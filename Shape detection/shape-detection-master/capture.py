import cv2 as cv
from filled_shape import filled_shape as fs
import argparse






if True:
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            fs.capture(frame)

        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break
    cap.release()
    cv.destroyAllWindows()
# elif arg.image_path is not None:
#     frame = cv.imread(arg.image_path.name)
#     fs.capture(frame, arg.debug)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
# else:
#     parser.parse_args(['--help'])

