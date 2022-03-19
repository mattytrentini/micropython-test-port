from sys import platform

if platform == 'renesas-ra':
    output_pin = "P105"
    input_pin = output_pin
    sda_pin = output_pin
    scl_pin = "P106"
    i2c_hard_id = 1
elif platform == 'rp2':
    output_pin = 1
    input_pin = output_pin
    sda_pin = output_pin
    scl_pin = 2
    i2c_hard_id = 1
else:
    raise ValueError("Platform not supported in check system.")


