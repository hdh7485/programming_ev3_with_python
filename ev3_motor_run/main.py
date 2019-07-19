#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

left_motor = Motor(Port.B)

left_motor.run_angle(360, 360, Stop.BRAKE, True)
wait(1000)

left_motor.run_angle(180, 180, Stop.BRAKE, True)
wait(1000)

left_motor.run_target(360, 0, Stop.BRAKE, True)
wait(1000)