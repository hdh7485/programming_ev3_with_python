#!/usr/bin/env pybricks-micropython

from math import sin

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
'''
left_motor.dc(30)
right_motor.dc(30)

while not any(brick.buttons()):
    brick.display.text('motor speed:' + str(left_motor.speed()))
    wait(10)
while any(brick.buttons()):
    wait(10)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.COAST)

while not any(brick.buttons()):
    brick.display.text('motor angle:' + str(left_motor.angle()))
    wait(10)
while any(brick.buttons()):
    wait(10)

left_motor.reset_angle(0)
brick.display.text('angle reset:' + str(left_motor.angle()))
while not any(brick.buttons()):
    wait(10)
while any(brick.buttons()):
    wait(10)

left_motor.run(100)
right_motor.run(100)
while not any(brick.buttons()):
    brick.display.text('motor speed:' + str(left_motor.speed()))
    wait(10)
while any(brick.buttons()):
    wait(10)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.COAST)

while not any(brick.buttons()):
    wait(10)
while any(brick.buttons()):
    wait(10)

left_motor.run_time(100, 1000, Stop.BRAKE, False)
right_motor.run_time(100, 1000, Stop.BRAKE, True)

while not any(brick.buttons()):
    wait(10)
while any(brick.buttons()):
    wait(10)

right_motor.reset_angle(0)
left_motor.run_angle(100, 360, Stop.BRAKE, False) #상대각도
right_motor.run_target(100, 360, Stop.BRAKE, False) #절대각도

while not any(brick.buttons()):
    brick.display.text(right_motor.angle())
    wait(10)
while any(brick.buttons()):
    wait(10)
'''
'''
right_motor.reset_angle(-1000)
left_motor.track_target(1000) #절대각도를 향해 가장 빠른 방법으로 모터 구동
right_motor.track_target(-1000) #절대각도

while not any(brick.buttons()):
    brick.display.text(right_motor.angle())
    wait(10)
while any(brick.buttons()):
    wait(10)

watch = StopWatch()
amplitude = 90
# In a fast loop, compute a reference angle
# and make the motor track it.
while True:
    # Get the time in seconds
    seconds = watch.time()/1000
    # Compute a reference angle. This produces
    # a sine wave that makes the motor move
    # smoothly between -90 and +90 degrees.
    angle_now = sin(seconds)*amplitude
    # Make the motor track the given angle
    left_motor.track_target(angle_now)
'''    
'''
left_motor.dc(40)
right_motor.dc(40)
wait(1000)
left_motor.set_dc_settings(100, 10) #두번째 파라메터 모름
left_motor.dc(3)
right_motor.dc(20)
wait(2000)
'''

#left_motor.dc(100)
#while not left_motor.stalled():
#    wait(1)
#left_motor.stop(Stop.BRAKE)
#right_motor.stop(Stop.BRAKE)
#
#left_motor.run_until_stalled(100, Stop.COAST)

# Set the maximum speed to 200 deg/s and acceleration to 400 deg/s/s.
left_motor.set_run_settings(600, 100)
# Make the motor run for 5 seconds. Even though the speed argument is 300
# deg/s in this example, the motor will move at only 200 deg/s because of
# the settings above.
left_motor.run_angle(600, 3600, Stop.BRAKE, False)
right_motor.run_angle(600, 3600, Stop.BRAKE, True)
