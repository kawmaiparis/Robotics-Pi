#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an NXT ultrasonic sensor connected to PORT_1 of the BrickPi3
# 
# Hardware: Connect an NXT ultrasonic sensor to BrickPi3 Port 1.
# 
# Results:  When you run this program, you should see the distance in CM.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers
import sys

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# Configure for an NXT ultrasonic sensor.
# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# BP.SENSOR_TYPE.NXT_ULTRASONIC specifies that the sensor will be an NXT ultrasonic sensor.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.NXT_ULTRASONIC)

stopping_distance = 30

def setPower(distance):
	distance = distance - stopping_distance                 
	if (distance > 100) :                                   # while the distance is above 
		BP.set_motor_power(BP.PORT_A, 75)
		BP.set_motor_power(BP.PORT_D, 75)
	elif (distance < 15 and distance > 0):                  # while robot is near object, slow it down.
		BP.set_motor_power(BP.PORT_A, 10)
		BP.set_motor_power(BP.PORT_D, 10)
	else :                                                  # stops the robot when it's at stopping distance
		BP.set_motor_power(BP.PORT_A, distance * 0.75)
		BP.set_motor_power(BP.PORT_D, distance * 0.75)

def turn(deg):
	start_posi_d = BP.get_motor_encoder(BP.PORT_D)
	start_posi_a = BP.get_motor_encoder(BP.PORT_A)
	BP.set_motor_power(BP.PORT_A, -20)
	BP.set_motor_power(BP.PORT_D, 20)
	while (int((abs(BP.get_motor_encoder(BP.PORT_D) - start_posi_d) + abs(BP.get_motor_encoder(BP.PORT_A) - start_posi_a))) < deg):
		a = 0
	calculateRotation()
		#print("A status: ", BP.get_motor_status(BP.PORT_A), " D status: ", BP.get_motor_status(BP.PORT_D))

def moveForward(cm):
	radius = 3.24
	circum = math.pi * 2 * radius
	revolution = cm / circum * 360 * 0.997
	start_posi = BP.get_motor_encoder(BP.PORT_D)
	BP.set_motor_power(BP.PORT_A, 30)
	BP.set_motor_power(BP.PORT_D, 30)
	while (abs(BP.get_motor_encoder(BP.PORT_D) - start_posi) < revolution):
		a = 0
	#	print("A status: ", BP.get_motor_status(BP.PORT_A), " D status: ", BP.get_motor_status(BP.PORT_D))
	calculateStraightLine(cm)

def stop():
	BP.set_motor_power(BP.PORT_A, 0)
	BP.set_motor_power(BP.PORT_D, 0)
	time.sleep(1)

try:
	while True:
		try: 
			value = BP.get_sensor(BP.PORT_1)
			#setPower(value)
			print(value)
		except brickpi3.SensorError as error:
			print(error)
		time.sleep(0.02)

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.



