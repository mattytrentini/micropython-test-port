# MicroPython High-Level Test Suite

The purpose of these tests is to determine whether a port conforms to providing MicroPython high-level features. It's especially useful to test new ports to see if their implementation is complete and correct.

## Running the test suite

```bash
micropython-test-port> mpremote connect <DEVICE> mount . exec "import overview"
```

## TODO
* framebuf
* SPI
* ADC
* I2S
* One wire
* Filesystem
* gc
* _thread
* Pin: drive
* UART: rx/tx
* Capacitive touch
* machine
  * machine.memX
  * Add bitstream/time_pulse_us to Neopixel tests?
  * enable/disable irq
  * deep/light sleep
  * reset_cause (tricky to thoroughly test)
  * unique_id
  * Signal
  * bootloader
  * soft/reset
* builtins (? Generally the same for all ports)
* pyb (?)
* I2C hard ids (take a list)
* SD card (see ESP32/stm)
* network
* Port-specific features
  * ESP32: RMT, ULP
  * stm: regsiters
  * rp2: PIO

Check parameters for each method?
