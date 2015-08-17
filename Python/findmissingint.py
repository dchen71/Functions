#Codility challenge which finds the missing element from a zero index array A consisting of N different intergers in range[1..(N+1)]

def solution(A):
    # write your code in Python 2.7
    start = 1
    answer = 1
    if len(A) == 0:
        answer = 1
    elif len(A) == 1:
        answer = 2
    else:
        for i in range(len(A)):
            if start == sorted(A)[i]:
                start += 1
            else:
                answer = start
                break
    
    return answer