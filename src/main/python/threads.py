
import time
import cv2 as cv 
from PyQt5.QtCore import QRunnable, pyqtSignal, pyqtSlot, QObject, Qt
from PyQt5.QtGui import QImage
from UI.Pages import page1

import globalvariables as gv
from ProcessImage.ocr_license_plate import processLP
from PIMG.ocr import OCRFrame



##################################################################
#region VIDEO THREAD

# initialize opencv video capture
url = 'http://192.168.43.1:8080/video'
cap = cv.VideoCapture(url)
# cap.set(3, gv.FeedWidth) # set width of video capture
# cap.set(4, gv.FeedHeight)  # set height of video capture

# define signals class
class FeedSignals(QObject):
    """
    Defines signals available while using camera feed thread..
    Signals:
        `frame` emits current frame of feed
    """
    processedImage = pyqtSignal(object, object)
    error = pyqtSignal(str)
    
# define worker
class FeedWorker(QRunnable):
    """
    Defines FeedWorker thread
    :param args: Arguments to make available to run thread
    :param kwargs: Keywords arguments to make available to run thread
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.args = args
        self.kwargs = kwargs
        self.signals = FeedSignals()

    # define run slot
    @pyqtSlot()
    def run(self):
        """
        Initialize the runner function of worker
        """
        try:
            while gv.VideoFeedStatus:
                ret, frame = cap.read()
                rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                if gv.ProcessFrame: # process frame if variable is true
                    # (lpText, img) = processLP(frame, debug=True)
                    (lpText, img) = OCRFrame(frame)
                    gv.ProcessFrame = False
                    print("inide thread")
                    self.signals.processedImage.emit(lpText, cv.cvtColor(img, cv.COLOR_BGR2RGB))
                    time.sleep(2)
                else:
                    self.signals.processedImage.emit(None,rgb_img)
        except Exception as e:
            self.signals.error.emit(str(e))
#endregion VIDEO THREAD
######################################################################
