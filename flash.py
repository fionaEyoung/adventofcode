import numpy as np
from scipy.ndimage import convolve

infile = 'input.txt'

energies = np.genfromtxt(infile, delimiter=1, dtype=int)
num_octos = np.prod(energies.shape)

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

    return flashed.sum()

nstep = 100
total_flashed = 0
for s in range(nstep):
    total_flashed += octo_step()

print(f"After {nstep} steps, {total_flashed} octos have flashed.")

while True:
    s += 1
    if octo_step() == num_octos:
        break

print(f"During step number {s+1}, all octos flashed at once!")