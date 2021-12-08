import numpy as np

data = np.loadtxt('input.txt')

diffs = np.diff(data)

print(diffs.size)

print("Number of increases: ", sum(diffs > 0)) 

sliding_sum = np.convolve(data, np.ones(3), 'valid')

print("Number of increases in sliding window: ", sum(np.diff(sliding_sum) > 0))
