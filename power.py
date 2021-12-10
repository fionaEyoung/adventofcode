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


def ox_rating(A, bit):
	
	if A.shape[0] == 1:
		return A[0]
	else:
		most_true = A[:,bit].sum() >= (A.shape[0] / 2)
		if most_true:
			new = A[ A[:, bit], :  ]    	
		else:
			new = A[ np.logical_not(A[:,bit]), :]
		
		return ox_rating(new, bit+1)


def co2_rating(A, bit):
	
	if A.shape[0] == 1:
		return A[0]
	else:
		most_false = A[:,bit].sum() < (A.shape[0] / 2)
		
		if most_false:
			new = A[ A[:, bit], :  ]    	
		else:
			new = A[ np.logical_not(A[:,bit]), :]
		
		return co2_rating(new, bit+1)


o = ox_rating(data, 0)
c = co2_rating(data, 0)

print("Oxygen rating: ", o)
print("CO2 rating: ", c)



life_support = (int( '0b' + ''.join(['1' if x else '0' for x in o]), 2) *
	 	int( '0b' + ''.join(['1' if x else '0' for x in c]), 2) )

print("Life support rating: ", life_support)


