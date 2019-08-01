#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

bool1 = 1 < 10
bool2 = 1 == 10
bool3 = 5 != 15

brick.display.text(bool1)
brick.display.text(bool2)
brick.display.text(bool3)

wait(3000)