import numpy as np
import csv


depth = 0
position = 0
aim = 0
with open('input.txt') as f:
	r = csv.reader(f, delimiter=' ')
	for row in r:
		x = int(row[1])
		if row[0] == 'forward':
			position += x
			depth += aim * x
		elif row[0] == 'up':
			aim -= x
		elif row[0] == 'down':
			aim += x

print("Final depth: ", depth)
print("Final position: ", position)
print("Solution: ", depth*position)
