import numpy as np
import csv


depth = 0
position = 0

with open('input.txt') as f:
	r = csv.reader(f, delimiter=' ')
	for row in r:
		if row[0] == 'forward':
			position += int(row[1])
		elif row[0] == 'up':
			depth -= int(row[1])
		elif row[0] == 'down':
			depth += int(row[1])

print("Final depth: ", depth)
print("Final position: ", position)
print("Solution: ", depth*position)
