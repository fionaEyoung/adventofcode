import numpy as np

infile = 'input.txt'

# Get number of lines
with open(infile) as f:
    n = sum(1 for line in f)

coords = np.zeros((n,2,2), dtype=int)
with open(infile) as f:
    for i, line in enumerate(f):
        coords[i] = np.array([ pair.split(',')
                     for pair in line.strip().split(' -> ')], dtype=int)


verticals = coords[ coords[:,0,0]==coords[:,1,0] ]
horizontals = coords[ coords[:,0,1]==coords[:,1,1] ]
diagonals = coords[ np.logical_and (coords[:,0,1]!=coords[:,1,1],
                                    coords[:,0,0]!=coords[:,1,0] )]

sz = np.amax(coords)
grid = np.zeros((sz+1,sz+1), dtype=int)

for v in verticals:
    grid[ v[0,0], min(v[:,1]):max(v[:,1])+1 ] += 1

for h in horizontals:
    grid[ min(h[:,0]):max(h[:,0])+1, h[0,1] ] += 1

for d in diagonals:
    grid[ range( d[0,0], d[1,0]+(-1)**(d[0,0]>d[1,0]),
                2*(d[0,0]<d[1,0])-1 ),
          range( d[0,1], d[1,1]+(-1)**(d[0,1]>d[1,1]),
                2*(d[0,1]<d[1,1])-1 )
          ] += 1

print(grid.T)
print("Number of overlapping points: ", np.count_nonzero(grid>1) )
