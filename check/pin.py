from machine import Pin
from config import output_pin, input_pin

# Check for init
#   - Output pin
#     - on/off/value
#   - Input pin
#     - value
#   - Various pull up/down

#p0 = Pin(config.output_pin, Pin.OUT)    # create output pin on GPIO0
p0 = Pin(output_pin, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
p0.off()                # set pin to "off" (low) level
p0.value(1)             # set pin to on/high

#p1 = Pin(config.input_pin, Pin.IN)     # create input pin on GPIO2
p1 = Pin(input_pin, Pin.IN)     # create input pin on GPIO2
print(p1.value())       # get value, 0 or 1

p2 = Pin(input_pin, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
#p2 = Pin(config.input_pin, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
p3 = Pin(output_pin, Pin.OUT, value=1) # set pin high on creation
#p3 = Pin(config.output_pin, Pin.OUT, value=1) # set pin high on creation

# Check for Pin.board
# Check for Pin.cpu