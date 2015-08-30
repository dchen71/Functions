# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 2.7
    s1 = area(K,L,M,N)
    s2 = area(P,Q,R,S)
    overlap = 0
    
    overlap = compute(K,L,M,N,P,Q,R,S)        
    
    total = s1 + s2 - overlap
    
    #-1 if function exceeds sum of 2147483647
    total = -1 if total >= 2147483647 else total
    
    return total

def compute(K,M,N,L,P, R, S, Q):
    overlap = 0
    
    #Inner dimensions
    in_x1 = 0
    in_x2 = 0
    in_y1 = 0
    in_y2 = 0
    
    if K <= P & P <= M:
        if N >= S & S >= L: #Top of B fits in
            if Q >= M:
                in_x2 = M
            else:
                in_x2 = Q
            in_y1 = N
            in_x1 = P
            if Q >= L: 
                if Q < N: #Assuming rectangle B completely fits inside
                    in_y2 = Q
            elif Q <= L: #Assuming x coords fit inside but y at bottom juts out
                in_y2 = L
        elif S > N:
            if Q >= M:
                in_x2 = M
                if N < Q & Q > L:
                    in_x2 = 0
            else:
                in_x2 = Q
            in_y1 = N
            in_x1 = P
            if Q <= L:
                in_y2 = L

            elif Q > L:
                in_y2 = Q
                if N < Q & Q > L:
                    in_y1 = 0
                    in_x1 = 0
        overlap = area(in_x1, in_y1, in_x2, in_y2)
    elif Q <= M:
        if S >= L:
            in_x2 = Q
        if K <= Q:
            in_x1 = K
        if S >= N & S >= L: #Checks if rect B diagonal is outside of the rect A
            in_y1 = N
            if Q >= L: 
                in_y2 = Q
            elif Q <= L: #Assuming x coords fit inside but y at bottom juts out
                in_y2 = L
        elif S <= N & S >= L:
            in_y1 = S
            if Q >= L: 
                in_y2 = Q
            elif Q <= L: #Assuming x coords fit inside but y at bottom juts out
                in_y2 = L
        overlap = area(in_x1, in_y1, in_x2, in_y2)

    return(overlap)

#Calculates area
def area(x1,y1,x2,y2):
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    return x * y