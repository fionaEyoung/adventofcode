import numpy as np

infile = 'input.txt'
init = np.loadtxt(infile, delimiter=',')

fish = init

ndays = 18

def lantern_fish(init, ndays):

    fish = init
    for d in range(ndays-1):

        # Check for iminent new fish
        new_fish = len(fish)-np.count_nonzero(fish)
        # Decrement counters
        fish -= 1
        fish = np.where ( fish == -1, 6, fish )
        # Add new fish
        if new_fish:
            fish = np.append(fish, [8]*new_fish)

    return fish


print("After 18 days: ", len(lantern_fish(init, 18)))
print("After 80 days: ", len(lantern_fish(init, 80)))