#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
touch_sensor = TouchSensor(Port.S1)

while(not touch_sensor.pressed()):
    left_motor.run(360)
    right_motor.run(360)
    wait(10)
while(touch_sensor.pressed()):
    wait(10)

left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)
wait(1000)