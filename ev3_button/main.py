#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

while True:
    if Button.CENTER in brick.buttons():
        brick.light(Color.RED)
    elif Button.LEFT in brick.buttons():
        brick.light(Color.GREEN)
    elif Button.RIGHT in brick.buttons():
        brick.light(Color.ORANGE)
    elif (Button.DOWN in brick.buttons()) and (Button.UP in brick.buttons()):
        brick.light(None)
