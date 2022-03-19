from machine import RTC

rtc = RTC()
awhile_ago = (2020, 8, 23, 2, 12, 48, 0, 0)
rtc.datetime(awhile_ago)
print("set time to: {}".format(awhile_ago))
print("time actual: {}".format(rtc.datetime()))
