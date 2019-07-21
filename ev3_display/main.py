#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

brick.display.text("Hello World", (60, 50))
wait(2000)
brick.display.clear()
brick.display.text(str(brick.battery.voltage()) + 'mV', (60, 50))
brick.display.text(str(brick.battery.current()) + 'mA', (60, 60))
wait(2000)
brick.display.image(ImageFile.UP)
wait(2000)
brick.display.image(ImageFile.UP', Align.LEFT, False)
wait(2000)
brick.display.image('figure.png', (100,0), True)
wait(2000)
