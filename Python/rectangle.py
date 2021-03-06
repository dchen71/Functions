#Finds the area of overlapping rectangles given array of points

def overlap(A,B):
    overlap = 0

    #Checks if input is a list
    if not isinstance(A, list) or not isinstance(B, list):
        return overlap

    #Validate that each point has 2 vertices
    if len(A) != 2:
        return overlap
    if len(B) != 2:
        return overlap
    if len(A[0]) < 2 | len(A[1]) < 2 | len(B[0]) < 2 | len(B[0]) < 2:
        print('length of array too short')
        return overlap

    #Validate that each diagonal makes a rectange(diagonal points arent equal)
    if A[0][0] == A[1][0] | A[0][1] == A[1][1] | B[0][0] == B[1][0] | B[0][1] == B[1][1]:
        return overlap

    #Separting the vertexes into easier to read variables and sorts them into top left to bottom right
    K = A[0][0] if A[0][0] < A[1][0] else A[1][0]
    N = A[0][1] if A[0][1] > A[1][1] else A[1][1]
    M = A[1][0] if A[1][0] > A[0][0] else A[0][0]
    L = A[1][1] if A[1][1] < A[0][1] else A[0][1]
    P = B[0][0] if B[0][0] < B[1][0] else B[1][0]
    S = B[0][1] if B[0][1] > B[1][1] else B[1][1]
    R = B[1][0] if B[1][0] > B[0][0] else B[0][0]
    Q = B[1][1] if B[1][1] < B[0][1] else B[0][1]


    #Tests whether or not the rectangles overlap and computes the overlap area
    #Will only work on non-directional rectangles
    overlap = compute(K, M, N, L, P, R, S, Q)
    overlap = compute(P, R, S, Q, K, M, N, L) if overlap == 0 else overlap

    return (overlap)

def area(A):
    return abs((A[0][0] - A[1][0]) * (A[0][1] - A[1][1]))

def compute(K,M,N,L,P, R, S, Q):
    overlap = 0

    #Interior variables
    in_x1 = 0
    in_x2 = 0
    in_y1 = 0
    in_y2 = 0

    if K <= P & P <= M:
        if N >= S & S >= L: #Top of B fits in
            if R >= M:
                in_x2 = M
            else:
                in_x2 = R
            in_y1 = N
            in_x1 = P
            if Q >= L: 
                if Q < N: #Assuming rectangle B completely fits inside
                    in_y2 = Q
            elif Q <= L: #Assuming x coords fit inside but y at bottom juts out
                in_y2 = L
        elif S > N:
            if R >= M:
                in_x2 = M
                if N < Q & Q > L:
                    in_x2 = 0
            else:
                in_x2 = R
            in_y1 = N
            in_x1 = P
            if Q <= L:
                in_y2 = L

            elif Q > L:
                in_y2 = Q
                if N < Q & Q > L:
                    in_y1 = 0
                    in_x1 = 0
        overlap = area([[in_x1, in_y1], [in_x2, in_y2]])
    elif R <= M:
        if S >= L:
            in_x2 = R
        if K <= R:
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
        overlap = area([[in_x1, in_y1], [in_x2, in_y2]])

    print(area(P,Q,R,S))
    return(overlap)

print(overlap([[0,2],[5,0]],[[-1,1],[1,-1]]))

#Testing
assert overlap([[1,1],[1,1]],[[2,2],[3,1]]) == 0 #No lines
assert overlap([[1,2],[4,-5]],[[2,2],[3,1]]) == 1 #Rectangle B completely fits inside A
assert overlap([[2,2],[3,1]],[[1,2],[4,-5]]) == 1 #Rectangle A completely fits inside B
assert overlap([[1,2],[4,-5]],[[1,2],[4,-5]]) == 21 #Rectangle B completely fits inside A
assert overlap([[1,2],[4,-5]],[[2,2],[3,-4]]) == 6 #Rectangle B stretches inside A
assert overlap([[1,2],[4,-5]],[[2,2],[3,3]]) == 0 #Rectangle B touchs but is not in A
assert overlap([[1,2],[4,-5]],[[2,2],[5,1]]) == 2 #Rectangle B stretches to the right past A
assert overlap([[1,2],[4,-5]],[[2,2],[5,-7]]) == 14 #Rectangle B stretches to bottom right
assert overlap([[1,2],[4,-5]],[[3,4],[7,1]]) == 1 #Part of a corner of B is in A
assert overlap([[1,2],[4,-5]],[[3,4],[7,-6]]) == 7 #Diagonal cuts through right part of rectangle A
assert overlap([[1,2],[4,-5]],[[-1,4],[2,1]]) == 1 #Part of a corner with diag is in A
assert overlap([[1,2],[4,-5]],[[-1,4],[2,-7]]) == 7 #Rectangle cuts in through left to part of Rect A
assert overlap([[1,2],[4,-5]],[[-1,-1],[2,-3]]) == 2 #Retangle B stretches into A from the left
assert overlap([[1,2],[4,-5]],[[-1,-4],[2,-6]]) == 1 #Rectangle B intersects from left
assert overlap([[1,50],[8,5]],[[-2,-2],[-5,-10]]) == 0 #Rectangles are not where close to each other
assert overlap([[-2,-2],[-5,-10]],[[1,50],[8,5]]) == 0 #Rectangles are not where close to each other
assert overlap([[1,50],[8,5]],[[0,5],[3,-10]]) == 0 #Rectangles are not where close to each other
assert overlap([[1,50],[8,5]],[[1,0],[5,-20]]) == 0 #Rectangles are not where close to each other
assert overlap('cat','dog') == 0 #Ensures only a list as the paramters
assert overlap([],[1,2]) == 0 #Ensures no empty lists
assert overlap([],[]) == 0 #Ensures no empty lists
