from machine import freq
from config import alt_freq

f = freq()
print(f"Default frequency is {f}")
if alt_freq:
    freq(alt_freq)  # Set alternate frequency
    if new_freq := freq() != alt_freq:
        raise ValueError(f"Frequency didn't change as expected. freq()={new_freq}")
    print(f"Alternate frequency set to {alt_freq}")
    freq(f) # Re-set default frequecy
