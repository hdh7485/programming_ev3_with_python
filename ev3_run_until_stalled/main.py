#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
left_motor.run_until_stalled(360, Stop.BRAKE) #모터의 최대 출력을 제한하지 않습니다.
wait(1000)
left_motor.run_until_stalled(360, Stop.BRAKE, 30) #모터의 최대 출력을 30%로 제한합니다.
wait(1000)