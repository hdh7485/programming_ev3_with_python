#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

number1 = 10
number2 = 20
number3 = number1 + number2
brick.display.text(number3)
wait(2000)

string1 = "Hello"
string2 = "hdh7485"
string3 = string1 + " " + string2
brick.display.text(string3)
wait(2000)

list1 = [500, 1000, 2000, 3000, 5000]
list2 = ["BTS", "itzy", 21]

brick.sound.beep(list1[0], 500, 100)
brick.sound.beep(list1[2], 500, 100)
brick.sound.beep(list1[4], 500, 100)

brick.display.text(list2)
wait(2000)