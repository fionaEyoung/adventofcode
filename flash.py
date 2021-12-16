import numpy as np
from scipy.ndimage import convolve

infile = 'example_input.txt'

energies = np.genfromtxt(infile, delimiter=1, dtype=int)

def octo_step():

    global energies
    flashed = np.zeros(energies.shape, dtype=bool)

    energies += 1

    while np.logical_and( (energies > 9),  ~flashed ).any():
        # Flash!
        flash = np.logical_and( (energies > 9),  ~flashed )
        # Ah-aaah
        energies += convolve( flash.astype(int), np.ones((3,3)), mode='constant' )
        flashed += flash

    energies[flashed] = 0

    print('\n'.join(
                    [''.join([str(i) if i else '.' for i in e])
                     for e in energies]
            )
          )
    return flashed.sum()

print("Initial: ")
print('\n'.join(
                [''.join([str(i) for i in e])
                 for e in energies]
        )
      )
print()
for s in range(5):
    print(f"After step {s}, {octo_step()} octos have flashed.\n")



