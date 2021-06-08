from PIMG import anpr 
import cv2 as cv


def OCRFrame(frame, debug=False):
    print('inside OCRFrame')
    npr = anpr.ImageSearchANPR(debug=debug)
    (lpText, result) = npr.processImg(frame)
    return(lpText, result)
if __name__ == "__main__":
    OCRFrame(cv.imread('Cars1.png'))