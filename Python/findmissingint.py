#Codility challenge which finds the missing element from a zero index array A consisting of N different intergers in range[1..(N+1)]

def solution(A):
    # write your code in Python 2.7
    start = 1
    answer = 1
    if len(A) == 0:
        answer = 1
    elif len(A) == 1:
        answer = 1
    else:
        sorted_arr = sorted(A)
        for i in sorted_arr:
            if start == i:
                start += 1
                if start == len(sorted_arr):
                    answer = start + 1
            else:
                answer = start
                break
    
    return answer