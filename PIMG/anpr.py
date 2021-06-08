
from skimage.segmentation import clear_border
from matplotlib import pyplot as plt
import pytesseract
import numpy as np
import imutils
import cv2 as cv


class ImageSearchANPR:
    def __init__(self, debug=False,):
        self.setps = []
        self.debug = debug
    ########################################################
    #region show steps
    def showStep(self, image, title,show=False,cols=2):
        '''This Function is used to view steps in image processing
        '''
        t = (image, title)
        self.setps.append(t)
        # print(len(self.setps))
        numOfStages = len(self.setps)
        rows = numOfStages // cols if numOfStages % cols == 0 else numOfStages // cols + 1

        if show and self.debug:
            for i in range(numOfStages):
                (image, title) = self.setps[i]
                plt.subplot(rows, cols, i+1)
                plt.axis('off')
                plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
                plt.title(title)
            plt.show()
    #endregion
    #########################################################

    ########################################################
    #region LP Detect
    def lp_detect(self, image, keep=10):
        img = image
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        edged = cv.Canny(gray, 30, 200)

        contours = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key = cv.contourArea, reverse=True)[:keep]
        screeCnt = None
        
        for c in contours:
            # approximate the contour
            peri = cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, 0.018 * peri, True)
            
            if len(approx) == 5:
                screeCnt = approx
                break
        
        # Masking the part other than number plate
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv.drawContours(mask, [screeCnt], 0, 255, -1)
        new_image = cv.bitwise_and(img, img, mask=mask)

        # Now Crop
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx + 1, topy:bottomy+1]
        return(Cropped, approx)
    
    #endregion 
    ############################################################

    def build_tesseract_options(self, psm=7):
        alphanumeric = "ABCDERGHIJKILMNOPQRSTUVWXYZ0123456789"
        options = "-c tessedit_char_whitelist={}".format(alphanumeric)

        # set PSM
        options += " --psm {}".format(psm)
        return options

    def clean_text(self, text):
        return "".join([c if ord(c) < 128 else "" for c in text]).strip()

    ########################################################
    #region Process Image
    def processImg(self, image, psm=7, clearBorder=False):
        '''Precess image and returs lpText and end result image'''
        print('inside process')
        (lp, location) = self.lp_detect(image)
        if lp is not None:
            options = self.build_tesseract_options(psm=psm)
            lpText = pytesseract.image_to_string(lp, lang="eng",config=options)

        if lpText is not None:
            font = cv.FONT_HERSHEY_SIMPLEX
            lpText = self.clean_text(lpText)
            resImg = cv.putText(image, text=lpText, org=(location[0][0][0], location[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv.LINE_AA)
            resImg = cv.rectangle(resImg, tuple(location[0][0]), tuple(location[2][0]), (0,255,0),2)

            print(lpText)
            return(lpText, resImg)
        else:
            return (None, image)
    #endregion
    #######################################################




