from skimage.segmentation import clear_border
import pytesseract
import numpy as np
import imutils
import cv2 as cv


class PyImageSearchANPR:
    '''Localises number plate and performs ocr
    '''
    def __init__(self, minAR=4, maxAR=5, debug=False):
        # store the minimum and maximum rectangular aspect ratio.
        # values along with whether or not we are in debug mode.
        self.minAR = minAR
        self.maxAR = maxAR
        self.debug = debug
    
    def debug_imshow(self, title, image, waitkey=False):
        # check to see if we are in debug mode, and if so show the 
        # image with the supplied title

        if self.debug:
            cv2.imshow(title, image)

            # check to see if we should wait for a keypress.
            if waitkey:
                cv2.waitKey(0)
    
    def locate_license_plate_candidates(self, gray, keep=5):
        '''Locates License plate area candidates
        @gray => grayscale image provide by driver script
        @keep => "up to this many" sorted license plate candidate contours.
        '''
        # Text will pop in image as light area
        rectKern = cv.getStructuringElement(cv.MORPH_RECT, (13, 5))
        blackhat = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, rectKern) # reveals dark characters against light backgrounds
        self.debug_imshow("Blackhat", blackhat)

        squareKern = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
        light = cv.morphologyEx(gray, cv.MORPH_CLOSE, squareKern)
        light = cv.threshold(light, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
        self.debug_imshow("Light Regions", light)

        








   