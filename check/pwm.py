# Test pwm

from machine import Pin, PWM
from config import output_pin

p = Pin(output_pin)
pwm = PWM(p)
pwm.freq()
pwm.freq(1000)
pwm.duty_u16()
pwm.duty_u16(200)
pwm.deinit()