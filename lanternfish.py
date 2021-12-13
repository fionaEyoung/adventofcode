import numpy as np
import matplotlib.pyplot as plt

infile = 'input.txt'
init = np.loadtxt(infile, delimiter=',')

n = 256

def lantern_fish(init, ndays):

    fish = np.zeros(9, dtype=int)
    for i in range(9):
        fish[i] = np.sum(init==i)

    for d in range(ndays):

        # Check for iminent new fish
        new_fish = fish[0]
        # Decrement counters (shift the buckets)
        fish = np.roll ( fish, -1 )
        # Add in the fish that just multiplied at 6
        fish[6] += fish[-1]

    return fish

print(f"After {n} days: ", sum(lantern_fish(init, n)))
