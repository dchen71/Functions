#Given a zero-indexed array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and 
#returns 0 otherwise.

def solution(A):
    triangle = 0
    points = [0,0,0]
    if len(A) >= 3:
        A.sort()
        for index in range(0, len(A) -2):
            if A[index] + A[index + 1] > A[index + 2]:
                triangle = 1
                break
    return triangle

assert(solution([10, 2, 5, 1, 8, 20])) == 1