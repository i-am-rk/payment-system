from os import terminal_size
from numpy.lib.twodim_base import _tri_dispatcher
from skimage.segmentation import clear_border
import pytesseract
import numpy as np
import imutils
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

class PyImageSearchANPR:
    '''Localises number plate and performs ocr
    '''
    def __init__(self, minAR=2, maxAR=6, debug=False):
        # store the minimum and maximum rectangular aspect ratio.
        # values along with whether or not we are in debug mode.
        self.minAR = minAR
        self.maxAR = maxAR
        self.debug = debug
    
    def debug_imshow(self, title, image, waitkey=False):
        # check to see if we are in debug mode, and if so show the 
        # image with the supplied title

        if self.debug:
            # cv.imshow(title, image)
            pil_img = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
            if waitkey:
                pil_img.show(title="test")

    #####################################################################
    #region Locate LP Candidates            
    def locate_license_plate_candidates(self, gray, keep=5):
        '''Locates License plate area candidates
        and returns list of likely contours containing license plates.

        @gray => grayscale image provide by driver script
        @keep => "up to this many" sorted license plate candidate contours.
        '''
        # perform morpholgical operation
        # reveal dark regions on light bakground
        # pop's up text in image
        rectKern = cv.getStructuringElement(cv.MORPH_RECT, (16, 5))
        blackhat = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, rectKern) # reveals dark characters against light backgrounds
        self.debug_imshow("Blackhat", blackhat,waitkey=True)


        # Find regions in imagae that are light
        squareKern = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
        light = cv.morphologyEx(gray, cv.MORPH_CLOSE, squareKern)
        light = cv.threshold(light, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
        self.debug_imshow("Light Regions", light)

        # compute teh scharr gradient representation of the blackhat
        # image in the x-direction and then scale the result back to
        # the range [0, 255]
        gradX = cv.Sobel(blackhat, ddepth=cv.CV_32F, dx=1, dy=0, ksize=-1)
        gradX = np.absolute(gradX)
        (minVal, maxVal) = (np.min(gradX), np.max(gradX))
        gradX = 255 * ((gradX - minVal) / (maxVal - minVal))
        gradX = gradX.astype("uint8")
        self.debug_imshow("Scharr", gradX,waitkey=True)

        # smooth the group regions that may contain boundries to license plate characters
        # blur the gradient representation, applying a closing 
        # operation, and threshold the image using Otsu's method

        gradX = cv.GaussianBlur(gradX, (5, 5), 0)
        gradX = cv.morphologyEx(gradX, cv.MORPH_CLOSE, rectKern)
        thresh = cv.threshold(gradX, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
        thresh = cv.erode(thresh, None, iterations=1)
        thresh = cv.dilate(thresh, None, iterations=1)
        self.debug_imshow("Grad Thresh", thresh, waitkey=True)

        # take the bitwise and between the threshold result and the
        # light regions of the image
        thresh = cv.bitwise_and(thresh, thresh, mask=light)
        thresh = cv.dilate(thresh, None, iterations=2)
        thresh = cv.erode(thresh, None, iterations=1)
        self.debug_imshow("final", thresh, waitkey=True)

        # find contours in the threshold image and sort them by 
        # their size in descending order, keeping only the largest
        # ones
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv.contourArea, reverse=True)[:keep]

        # return the list of countours
        return cnts
    #endregion Locate LP Candidates
    ####################################################################
    
    ###############################################################
    #region Locate LP
    def locate_license_plate(self, gray, candidates, clearBorder=False):
        '''Locate license plate from the list of contours of likely candidates
        '''
        # initialize the license plate contour and ROI
        lpCnt = None
        roi = None

        # loop over the license plate candidate contours
        for c in candidates:
            # compute the bonding box of the contour and the use
            # the bounding box to derive the aspect ratio
            (x, y, w, h) = cv.boundingRect(c)
            ar = w / float(h) # aspect ratio of bounding Rect

            # check to see if the aspect ratio is reactangular
            if ar >= self.minAR and ar <= self.maxAR:
                # store the license plate contour and extract the
                # licenseplate from gray scale image and then
                # threshold it
                lpCnt = c
                licensePlate = gray[y:y + h, x:x + w]
                roi = cv.threshold(licensePlate, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]

                # check to see if we should clear any forground
                # pixels touching the border of the image
                #(which typically, not but always, indicates noise)

                if clearBorder:
                    roi = clear_border(roi)

                # display the debugging information and then break
                # from the loop early since we have found the license
                #plate region
                self.debug_imshow("Licese Plate", licensePlate)
                self.debug_imshow("ROI", roi)
                break
        
        # return a 2-tuple of the license plate ROI and the contour
        # associated with it.
        return (roi, lpCnt)
    #endregion Locate LP
    ###############################################################

    ###############################################################
    #region Tesseract Option
    def build_tesseract_options(self, psm=7):
        # tell Tesseract to only OCR alphanumeric characters
        alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        options = "-c tessedit_char_whitelist={}".format(alphanumeric)

        # set PSM mode
        options += " --psm {}".format(psm)
        return options
    #endregion Tesseract Option
    ###############################################################

    ###########################################################
    #region Find and OCR
    def find_and_ocr(self, image, psm=7, clearBorder=False):
        # initialize the license plate text
        lpText = None
        # convert the input image to grayscale, locate all candidate
        # license plate regions in the image, and then process the 
        # candidates, leaving us with the *actual* license plate
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        candidates = self.locate_license_plate_candidates(gray)
        (lp, lpCnt) = self.locate_license_plate(gray, candidates, clearBorder=clearBorder)
        # only OCR the license plate if the license plate ROI is not 
        # empty
        if lp is not None:
            # OCR the license plate
            options = self.build_tesseract_options(psm=psm)
            lpText = pytesseract.image_to_string(lp, config=options)
            self.debug_imshow("License Plate", lp, waitkey=True)
        
        return (lpText, lpCnt)
    #endregion Find and OCR
    #############################################################






   