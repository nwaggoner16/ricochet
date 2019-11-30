import RPi.GPIO as GPIO
import time

class L298n:
	def __init__(self, ena_pin, in1_pin, in2_pin, in3_pin, in4_pin, speed, run_time):
		self.ena_pin = ena_pin
		self.in1_pin = in1_pin
		self.in2_pin = in2_pin
		self.in3_pin = in3_pin
		self.in4_pin = in4_pin
		self.speed = speed
		self.run_time = run_time
	def forward(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.ena_pin, GPIO.OUT)
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		GPIO.setup(self.in3_pin, GPIO.OUT)
		GPIO.setup(self.in4_pin, GPIO.OUT)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
		pump = GPIO.PWM(self.ena_pin, 1000)
		pump.start(self.speed)
		GPIO.output(self.in1_pin, GPIO.HIGH)
		GPIO.output(self.in3_pin, GPIO.HIGH)
		time.sleep(self.run_time)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in3_pin, GPIO.LOW)
		GPIO.cleanup()
	def reverse(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.ena_pin, GPIO.OUT)
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		GPIO.setup(self.in3_pin, GPIO.OUT)
		GPIO.setup(self.in4_pin, GPIO.OUT)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
		pump = GPIO.PWM(self.ena_pin, 1000)
		pump.start(self.speed)
		GPIO.output(self.in2_pin, GPIO.HIGH)
		GPIO.output(self.in4_pin, GPIO.HIGH)
		time.sleep(self.run_time)
		GPIO.output(self.in2_pin, GPIO.LOW)
		GPIO.output(self.in4_pin, GPIO.LOW)
		GPIO.cleanup()
	def left(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.ena_pin, GPIO.OUT)
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		GPIO.setup(self.in3_pin, GPIO.OUT)
		GPIO.setup(self.in4_pin, GPIO.OUT)
		GPIO.output(self.in3_pin, GPIO.LOW)
		GPIO.output(self.in4_pin, GPIO.LOW)
		pump = GPIO.PWM(self.ena_pin, 1000)
		pump.start(self.speed)
		GPIO.output(self.in3_pin, GPIO.HIGH)
		#GPIO.output(self.in4_pin, GPIO.HIGH)
		time.sleep(self.run_time)
		GPIO.output(self.in3_pin, GPIO.LOW)
		#GPIO.output(self.in4_pin, GPIO.LOW)
		GPIO.cleanup()
	def right(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.ena_pin, GPIO.OUT)
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		GPIO.setup(self.in3_pin, GPIO.OUT)
		GPIO.setup(self.in4_pin, GPIO.OUT)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
		pump = GPIO.PWM(self.ena_pin, 1000)
		pump.start(self.speed)
		GPIO.output(self.in1_pin, GPIO.HIGH)
		#GPIO.output(self.in3_pin, GPIO.HIGH)
		time.sleep(self.run_time)
		GPIO.output(self.in1_pin, GPIO.LOW)
		#GPIO.output(self.in3_pin, GPIO.LOW)
		GPIO.cleanup()
		
Robo_car = L298n(22,18,16,12,11,100,1)
#Robo_car.reverse()
movement = 'n'
while(1):
	movement = raw_input()
	if movement == 'w':
		Robo_car.forward()
	elif movement == 's':
		Robo_car.reverse()
	elif movement == 'a':
		Robo_car.left()
	elif movement == 'd':
		Robo_car.right()
	elif movement == 'n':
		GPIO.cleanup()
