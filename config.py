from sys import platform

if platform == 'renesas-ra':
    output_pin = "P105"
    input_pin = output_pin
    sda_pin = output_pin
    scl_pin = "P106"
    i2c_hard_id = 1
    alt_freq = 100_000_000
elif platform == 'rp2':
    output_pin = 1
    input_pin = output_pin
    sda_pin = output_pin
    scl_pin = 2
    i2c_hard_id = 1
    alt_freq = 48_000_000
elif platform == 'esp32':
    output_pin = 10
    input_pin = output_pin
    sda_pin = 4
    scl_pin = 5
    i2c_hard_id = 0
    alt_freq = 160_000_000
elif platform == 'Realtek Ameba':
    output_pin = "PB_4"
    input_pin = output_pin
    sda_pin = "PB_6"
    scl_pin = "PB_5"
    i2c_hard_id = 0
    alt_freq = 160_000_000
else:
    raise ValueError("Platform not supported in check system.")


