# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    triangle = 0
    points = [0,0,0]
    if len(A) >= 3:
        A.sort()
        for index in xrange(0, len(A) -2):
            if A[index] + A[index + 1] > A[index + 2]:
                triangle = 1
                break
    return triangle