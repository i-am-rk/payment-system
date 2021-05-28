from os import WIFCONTINUED, terminal_size
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
                pil_img.show(title=title)

    #####################################################################
    #region Locate LP Candidates            
    def locate_license_plate_candidates(self, gray, keep=20):
        '''Locates License plate area candidates
        and returns list of likely contours containing license plates.

        @gray => grayscale image provide by driver script
        @keep => "up to this many" sorted license plate candidate contours.
        '''
        gray = cv.bilateralFilter(gray, 11, 17, 17)
        edged = cv.Canny(gray, 170, 200)

        cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
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
            peri = cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, 0.02 * peri, True)

            # compute the bonding box of the contour and the use
            # the bounding box to derive the aspect ratio
            (x, y, w, h) = cv.boundingRect(c)
            ar = w / float(h) # aspect ratio of bounding Rect
            arTF = ar >= self.minAR and ar <= self.maxAR
            # check to see if the aspect ratio is reactangular
            if arTF and w > 180:
                lpCnt = c
                licensePlate = gray[y:y + h, x:x + w]
                roi = cv.threshold(licensePlate, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]


                # check to see if we should clear any forground
                # pixels touching the border of the image
                #(which typically, not but always, indicates noise)
                # self.warp_lp(roi)
                if clearBorder:
                    roi = clear_border(roi)
                # display the debugging information and then break
                # from the loop early since we have found the license
                #plate region
                print(cv.boundingRect(c), cv.contourArea(c))
                self.debug_imshow("Licese Plate", licensePlate)
                self.debug_imshow("ROI", roi, waitkey=True)
                break
        return (roi, lpCnt)
    #endregion Locate LP
    ###############################################################

    #################################################################
    #region warp image  
    # def warp_lp(self, img):
    #     kernal = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    #     dilate = cv.dilate(img, kernal, iterations=3)
    #     canny = cv.Canny(dilate, 0, 255, 1)

    #     corners = cv.cv2.goodFeaturesToTrack(canny,4,0.01,10)
    #     corners = np.int0(corners)
    #     print(corners)
    #     for corner in corners:
    #         (x,y) = corner.ravel()
    #         cv.circle(dilate, (x, y), 10, (0, 255, 0), -1)

    #     self.debug_imshow("dilate", canny, waitkey=True)
    #     self.debug_imshow("dilate", dilate, waitkey=True)
    #endregion warp image   
    ##############################################################

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
            lpText = pytesseract.image_to_string(lp,lang="eng",config=options)
            self.debug_imshow("License Plate", lp, waitkey=False)
        
        return (lpText, lpCnt)
    #endregion Find and OCR
    #############################################################






   