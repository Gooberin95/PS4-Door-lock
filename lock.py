import RPi.GPIO as GPIO
import time
from pyPS4Controller.controller import Controller
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    def on_x_press(self):
        GPIO.output(32,GPIO.LOW)

    def on_square_press(self):
        GPIO.output(32,GPIO.HIGH)





controller = MyController(interface='/dev/input/js0', connecting_using_ds4drv=False)
controller.listen()
