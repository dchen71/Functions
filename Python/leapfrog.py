# you can use print for debugging purposes, e.g.
# print "this is a debug message"
import math

def solution(X, Y, D):
    # write your code in Python 2.7
    jump = 0
    if X < Y:
        jump = int(math.ceil((Y-X)/float(D)))
    return jump