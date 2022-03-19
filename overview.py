
def section(title, pre="\n"):
    print("{}==== {} ====\n".format(pre, title))

section("Platform", pre="")
import sys
print("Platform: {}".format(sys.platform))
print("Implementation: {}".format(sys.implementation))

section("modules and dir")
import machine
help("modules")
print("\n  -- dir() --\n{}".format(dir()))
print("\n  -- dir(machine) --\n{}".format(dir(machine)))


def check_feature(title, import_name):
    section(title)
    try:
        __import__(import_name)
    except:
        print("Problem importing", title)

check_feature("machine.Pin", "check.pin")

check_feature("machine.PWM", "check.pwm")

check_feature("machine.SoftI2C", "check.i2c_soft")

check_feature("machine.I2C", "check.i2c_hard")

check_feature("machine.rtc", "check.rtc")

check_feature("fstrings", "check.fstrings")

check_feature("time", "check.time")

check_feature("Neopixel Support", "check.neopixel")

check_feature("WDT", "check.wdt")
