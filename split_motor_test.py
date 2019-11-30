import RPi.GPIO as GPIO
import time
import keyboard

class l298n:
	def __init__(self, ena_pin, enb_pin, in1_pin, in2_pin, in3_pin, in4_pin, speed, run_time):
		self.ena_pin = ena_pin
		self.enb_pin = enb_pin
		self.in1_pin = in1_pin
		self.in2_pin = in2_pin
		self.in3_pin = in3_pin
		self.in4_pin = in4_pin
		self.speed = speed
		self.run_time = run_time
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.ena_pin, GPIO.OUT)
		GPIO.setup(self.enb_pin, GPIO.OUT)
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		GPIO.setup(self.in3_pin, GPIO.OUT)
		GPIO.setup(self.in4_pin, GPIO.OUT)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
		GPIO.output(self.in3_pin, GPIO.LOW)
		GPIO.output(self.in4_pin, GPIO.LOW)
		
	def forward(self):
		motor1 = GPIO.PWM(self.enb_pin, 1000)
		motor1.start(self.speed)
		motor2 = GPIO.PWM(self.ena_pin, 1000)
		motor2.start(self.speed)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in3_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.HIGH)
		GPIO.output(self.in4_pin, GPIO.HIGH)
		time.sleep(self.run_time)
		
		
	
	def reverse(self):
		motor1 = GPIO.PWM(self.enb_pin, 1000)
		motor1.start(self.speed)
		motor2 = GPIO.PWM(self.ena_pin, 1000)
		motor2.start(self.speed)
		GPIO.output(self.in2_pin, GPIO.LOW)
		GPIO.output(self.in4_pin, GPIO.LOW)
		GPIO.output(self.in1_pin, GPIO.HIGH)
		GPIO.output(self.in3_pin, GPIO.HIGH)
		time.sleep(self.run_time)
		
	def right(self):
		motor1 = GPIO.PWM(self.enb_pin, 1000)
		motor1.start(self.speed)
		motor2 = GPIO.PWM(self.ena_pin, 1000)
		motor2.start(self.speed)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in3_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.HIGH)
		GPIO.output(self.in4_pin, GPIO.LOW)
		time.sleep(self.run_time)
		
	def left(self):
		motor1 = GPIO.PWM(self.enb_pin, 1000)
		motor1.start(self.speed)
		motor2 = GPIO.PWM(self.ena_pin, 1000)
		motor2.start(self.speed)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in3_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
		GPIO.output(self.in4_pin, GPIO.HIGH)
		time.sleep(self.run_time)

ricochet = l298n(22, 15, 18,16,12,11,90,1)
	
"""ricochet.forward()
ricochet.reverse()
ricochet.right()
ricochet.left()
GPIO.cleanup()"""

movement = 'n'
while(1):
	movement = raw_input()
	if movement == 'w':
		ricochet.forward()
	elif movement == 's':
		ricochet.reverse()
	elif movement == 'a':
		ricochet.left()
	elif movement == 'd':
		ricochet.right()
	elif movement == 'n':
		GPIO.cleanup()
		


"""while(1):
	if keyboard.is_pressed('w'):
		#ricochet.forward()
		print('yes')
		GPIO.cleanup()"""
        
 

	

