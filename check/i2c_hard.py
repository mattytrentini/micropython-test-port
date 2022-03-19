from machine import I2C
from config import i2c_hard_id

i2c = I2C(i2c_hard_id)  # create software I2C object

# i2c.scan()                          # returns list of peripheral addresses
# i2c.writeto(0x42, 'hello')          # write 5 bytes to peripheral with address 0x42
# i2c.readfrom(0x42, 5)               # read 5 bytes from peripheral

# i2c.readfrom_mem(0x42, 0x10, 2)     # read 2 bytes from peripheral 0x42, peripheral memory 0x10
# i2c.writeto_mem(0x42, 0x10, 'xy')   # write 2 bytes to peripheral 0x42, peripheral memory 0x10

# change freq?
# deinit?