#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

count = 0
while count < 10:
    brick.display.clear()
    brick.display.text(count, (50, 60))
    wait(500)
    count = count + 1
    #count += 1

for i in range(10):
    brick.display.clear()
    brick.display.text(i, (50, 60))
    wait(500)