# MicroPython High-Level Test Suite

The purpose of these tests is to determine whether a port conforms to providing MicroPython high-level features. It's especially useful to test new ports to see if their implementation is complete and correct.

## Running the test suite

```bash
micropython-test-port>mpremote connect <DEVICE> mount . exec "import overview"
```