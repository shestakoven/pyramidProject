import datetime
import os
from time import sleep

import cv2
import pyramid_basemodel
import transaction

from pyramidProject.models import Capture

TIME_FORMAT = "%d-%m-%Y_%H:%M:%S"
PATH_TO_FOLDER = os.path.join('pyramidProject', 'media')
# Вместо "0" указать адрес камеры, например rtsp://username:password@192.168.1.2/h264_stream
PATH_TO_CAM = 0
# Период сохранения изображения с камеры
SAVE_PERIOD = 15


def main():
    """Connect to camera and save capture,"""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        filename = f'cap{datetime.datetime.now().strftime(TIME_FORMAT)}.jpeg'
        filepath = os.path.join(
            PATH_TO_FOLDER,
            filename,
        )
        cv2.imwrite(filepath, frame)

        model_capture = Capture(
            path=f'media/{filename}',
            camera=PATH_TO_CAM
        )
        pyramid_basemodel.Session.add(model_capture)
        transaction.commit()
        sleep(SAVE_PERIOD)
