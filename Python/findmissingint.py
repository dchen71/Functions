#Codility challenge which finds the missing element from a zero index array A consisting of N different intergers in range[1..(N+1)]

def solution(A):
    # write your code in Python 2.7
    start = 1
    answer = 0
    for i in range(len(A)):
        if start == sorted(A)[i]:
            start += 1
        else:
            answer = i + 1
            break
    
    return answer