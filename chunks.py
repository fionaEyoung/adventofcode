import numpy as np


infile = 'input.txt'

data = [line.strip() for line in open(infile)]



stack1 = [] # ()
stack2 = [] # []
stack3 = [] # {}
stack4 = [] # <>

def check_line(s):

    openers = {'(': 3, '[': 57, '{': 1197, '<': 25137}
    closers = {')':-3, ']':-57, '}':-1197, '>':-25137}
    stack = []

    for c in s:

        if c in openers.keys():
            stack.append(c)

        elif c in closers.keys():
            if not openers[ stack[-1] ] + closers[c]:
                # Closing character completes top of stack -> pop off
                stack.pop()
            else:
                # Mismatching character -> return score from function
                return 0, abs(closers[c])

    # Reached the end of the line.
    # If the stack is not empty, return False (incomplete)
    if len(stack):

        points = {'(': 1, '[': 2, '{': 3, '<': 4}
        score = 0
        while stack:
            score *= 5
            score += points[ stack.pop() ]

        return 1, score

    else:
    # The line is sound, no syntax errors
        return 3


results = [list(check_line(s)) for s in data ]

print("Total syntax error score for corrupted lines: ",
      sum([r[1] for r in results if r[0]==0]) )

incompletes = [r[1] for r in results if r[0]==1]
incompletes.sort()

print("Middle syntax error score for incomplete lines: ",
      incompletes[ len(incompletes) //2 ])