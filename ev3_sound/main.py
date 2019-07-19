#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()
wait(1000)
brick.sound.beep(300, 1000, 50)
wait(1000)
brick.sound.beep(8000, 2000, 100)
wait(1000)
brick.sound.beeps(5)
wait(1000)
brick.sound.file(SoundFile.HELLO)
