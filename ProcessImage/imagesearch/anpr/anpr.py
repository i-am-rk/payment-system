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
    def __init__(self, minAR=3, maxAR=7, debug=False):
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
        gray = cv.bilateralFilter(gray, 11, 17, 17)
        edged = cv.Canny(gray, 170, 200)

        cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv.contourArea, reverse=True)[:30]

        # return the list of countours
        return cnts
    #endregion Locate LP Candidates
    ####################################################################
    
    ###############################################################
    #region Locate LP
    def locate_license_plate(self, gray, candidates, clearBorder=True):
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
                self.debug_imshow("Licese Plate", licensePlate, waitkey=True)
                self.debug_imshow("ROI", roi, waitkey=True)
                break
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






   