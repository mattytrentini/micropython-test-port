print("Watchdog support: ", end="")
try:
    from machine import WDT
except ImportError:
    print(False)
else:
    print(True)
