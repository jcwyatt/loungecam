from time import sleep
import picamera


with picamera.PiCamera() as camera:
    camera.start_preview()
    sleep(10)
    for filename in camera.capture_continuous('loungecam.jpg'):
        print('Captured %s' % filename)
        sleep(10)
