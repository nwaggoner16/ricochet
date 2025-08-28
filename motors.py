import pigpio
import time
from ps4remote import controller

motorconn = pigpio.pi('localhost', 8888)
if not motorconn.connected:
    raise Exception("Could not connect to pigpio daemon!")  

max_speed = 480

m1flt = 5
m2flt = 6
m1pwm = 12
m2pwm = 13
m1en = 22
m2en = 23


class Motor(object):
    def __init__(self, pwm_pin, en_pin, flt_pin, dir_pin):
        self.pwm_pin = pwm_pin
        self.en_pin = en_pin
        self.flt_pin = flt_pin
        self.dir_pin = dir_pin

        motorconn.set_pull_up_down(self.flt_pin, pigpio.PUD_UP)
        motorconn.write(self.en_pin, 1)

    def set_speed(self, speed):
        if speed > max_speed:
            speed = max_speed
        elif speed < -max_speed:
            speed = -max_speed

        if speed < 0:
            speed = -speed
            if self.dir_pin is not None:
                motorconn.write(self.dir_pin, 1)
        else:
            if self.dir_pin is not None:
                motorconn.write(self.dir_pin, 0)

        motorconn.set_PWM_dutycycle(self.pwm_pin, speed)

    def get_fault(self):
        return motors.read(self.flt_pin) == 0

motor1 = Motor(m1pwm, m1en, m1flt, None)

motor1.set_speed(0)
time.sleep(5000)
motor1.set_speed(0)