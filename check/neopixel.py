print("Neopixel support: ", end="")
try:
    from neopixel import NeoPixel
except ImportError:
    print(False)
else:
    print(True)
