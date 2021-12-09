import numpy as np

n = 1000
b = 12
filename = 'input.txt'
data = np.empty((n,b), dtype=bool)

with open(filename) as f:
	i = 0
	for line in f:
		if not line:
			break
		data[i,:] = np.array([c=='1' for c in line.strip()])	
		i+=1

gamma = data.sum(axis=0) > (n/2)
epsilon = np.logical_not(gamma)
print(gamma)
print(epsilon)
power = (int( '0b' + ''.join(['1' if x else '0' for x in gamma]), 2) *
	 int( '0b' + ''.join(['1' if x else '0' for x in epsilon]), 2) )

print("Power = ", power)
