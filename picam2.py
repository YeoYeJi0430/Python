# import picamera

# with picamera.PiCamera() as cam:
#     cam.resolution = (640, 480) #해상도
#     cam.start_preview()
#     cam.start_recording('foo.h264')
#     cam.wait_recording(60)
#     cam.stop_recording()
#     cam.stop_preview()

import time
import picamera

with picamera.PiCamera() as cam:
    cam.resolution = (1280, 720)
    cam.start_preview()
    cam.exposure_compensation = 2
    cam.exposure_mode = 'spotlight'
    cam.meter_mode = 'matrix'
    cam.image_effect = 'gpen'
    time.sleep(2)
    cam.exif_tags['IFD0.Artist'] = 'Kim'
    cam.exif_tags['IFD0.Copyright'] = 'CopyleftKim'
    cam.capture('foo.jpg')
    cam.stop_preview()