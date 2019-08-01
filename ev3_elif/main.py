#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


sonar = UltrasonicSensor(Port.S2)
motor_left = Motor(Port.B)
motor_right = Motor(Port.C)

while True:
    distance = sonar.distance()
    if distance >= 500:
        motor_left.dc(100)
        motor_right.dc(100)
    elif distance >= 300:
        motor_left.dc(70)
        motor_right.dc(70)
    elif distance >= 100:
        motor_left.dc(30)
        motor_right.dc(30)
    else:
        motor_left.dc(0)
        motor_right.dc(0)