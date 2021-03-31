
import cv2 as cv 
from PyQt5.QtCore import QRunnable, pyqtSignal, pyqtSlot, QObject, Qt
from PyQt5.QtGui import QImage


import globalvariables as gv



##################################################################
#region VIDEO THREAD

# initialize opencv video capture
cap = cv.VideoCapture(0)
cap.set(3, gv.FeedWidth) # set width of video capture
cap.set(4, gv.FeedHeight)  # set height of video capture

# define signals class
class FeedSignals(QObject):
    """
    Defines signals available while using camera feed thread.
    Signals:
        `frame` emits current frame of feed
    """
    cv_image = pyqtSignal(object)
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

        print("inside worker init")
    # define run slot

    @pyqtSlot()
    def run(self):
        """
        Initialize the runner function of worker
        """
        # for n in range(10):
        #     print(n)
        # print("inside worker run")
        try:
            while gv.VideoFeedStatus:
                ret, frame = cap.read()
                rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                self.signals.cv_image.emit(rgb_img)

        except Exception as e:
            self.signals.error.emit(str(e))
        
        # def cv_to_pixmap(cvimage):
        #     """Convert opencv image to QPixmap"""
        #     print("cv_to_pixmap")
        #     h, w, ch = cvimage.shape # get shape of image
        #     bytes_per_line = ch * w
        #     convert_to_Qt_format = QImage(cvimage, w, h, bytes_per_line, QImage.Format_RGB888)
        #     return convert_to_Qt_format


#endregion VIDEO THREAD
######################################################################
