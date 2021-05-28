from imagesearch.anpr.anpr import PyImageSearchANPR
# from ProcessImage.imagesearch.anpr.anpr import PyImageSearchANPR
from imutils import paths
from PIL import Image
import argparse
import imutils
import cv2 as cv







def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using opencv
    print(text)
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def showImage(image):
    pil_img = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    pil_img.show("Final")
############################################################3
#region processLP
def processLP(image,debug=True):
    anpr = PyImageSearchANPR(debug=debug)
    # image = imutils.resize(image, width=800)

    # apply automatic license plate recognition
    (lpText, lpCnt) = anpr.find_and_ocr(image)
    # only continue if the license plate was successfully OCR'd
    if lpText is not None and lpCnt is not None:
        # fit a rotated bounding box to the license plate contour and
        # draw the bounding box on the license plate
        box = cv.boxPoints(cv.minAreaRect(lpCnt))
        box = box.astype("int")
        cv.drawContours(image, [box], -1, (0, 255, 0), 2)

        # compute a normal(unrotated) bounding box for the license plate
        # and then draw the OCR'd license plate text on the image
        (x,y, w, h) = cv.boundingRect(lpCnt)
        cv.putText(image, cleanup_text(lpText), (x, y -15), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)


        # print output
        print("[INFO] {}".format(lpText))
    return(lpText, image)
#endregion processLP
###############################################################

def main(k):
    image = cv.imread('ProcessImage/license_plates/Cars3.png')
    (text, image) = processLP(image)
    showImage(image)
if __name__ == "__main__":
    main("test")