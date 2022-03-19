import time
try:
    start = time.ticks_us() # get microsecond counter
    time.sleep(1)           # sleep for 1 second
    time.sleep_ms(500)      # sleep for 500 milliseconds
    time.sleep_us(10)       # sleep for 10 microseconds
    delta = time.ticks_diff(time.ticks_us(), start) # compute time difference
    print("Should have slept for 1500010 microseconds, actual = {}, diff = {}".format(delta, delta-1_500_010))
except AttributeError:
    print("Some time methods not present")
