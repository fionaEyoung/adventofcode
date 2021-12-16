import numpy as np

infile = 'example_input.txt'

data = np.loadtxt(infile, delimiter='')
print(data)