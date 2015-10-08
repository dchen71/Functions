# Given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
import math

def solution(X, Y, D):
    jump = 0
    if X < Y:
        jump = int(math.ceil((Y-X)/float(D)))
    return jump

assert(solution(10, 85, 30)) == 3