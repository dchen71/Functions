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
    A_x1 = A[0][0] if A[0][0] < A[1][0] else A[1][0]
    A_y1 = A[0][1] if A[0][1] > A[1][1] else A[1][1]
    A_x2 = A[1][0] if A[1][0] > A[0][0] else A[0][0]
    A_y2 = A[1][1] if A[1][1] < A[0][1] else A[0][1]
    B_x1 = B[0][0] if B[0][0] < B[1][0] else B[1][0]
    B_y1 = B[0][1] if B[0][1] > B[1][1] else B[1][1]
    B_x2 = B[1][0] if B[1][0] > B[0][0] else B[0][0]
    B_y2 = B[1][1] if B[1][1] < B[0][1] else B[0][1]

    #Interior variables
    in_x1 = 0
    in_x2 = 0
    in_y1 = 0
    in_y2 = 0

    #Tests whether or not the rectangles overlap and computes the overlap area
    #Will only work on non-directional rectangles
    if A_x1 <= B_x1 & B_x1 <= A_x2:
        in_x1 = B_x1
        if B_x2 >= A_x2:
            in_x2 = A_x2
        else:
            in_x2 = B_x2
        
        if A_y1 >= B_y1 & B_y1 >= A_y2: #Top of B fits in
            in_y1 = A_y1
            if B_y2 >= A_y2: 
                if B_y2 < A_y1: #Assuming rectangle B completely fits inside
                    in_y2 = B_y2
            elif B_y2 <= A_y2: #Assuming x coords fit inside but y at bottom juts out
                in_y2 = A_y2
        elif B_y1 > A_y1:
            in_y1 = A_y1
            if B_y2 <= A_y2:
                in_y2 = A_y2
            elif B_y2 > A_y2:
                in_y2 = B_y2
        overlap = area([[in_x1, in_y1], [in_x2, in_y2]])
    elif B_x2 <= A_x2:
        if B_y1 >= A_y2:
            in_x2 = B_x2
        if A_x1 <= B_x2:
            in_x1 = A_x1
        if B_y1 >= A_y1 & B_y1 >= A_y2: #Checks if rect B diagonal is outside of the rect A
            in_y1 = A_y1
            if B_y2 >= A_y2: 
                in_y2 = B_y2
            elif B_y2 <= A_y2: #Assuming x coords fit inside but y at bottom juts out
                in_y2 = A_y2
        elif B_y1 <= A_y1 & B_y1 >= A_y2:
            in_y1 = B_y1
            if B_y2 >= A_y2: 
                in_y2 = B_y2
            elif B_y2 <= A_y2: #Assuming x coords fit inside but y at bottom juts out
                in_y2 = A_y2
        overlap = area([[in_x1, in_y1], [in_x2, in_y2]])


    return (overlap)

def area(A):
    return abs((A[0][0] - A[1][0]) * (A[0][1] - A[1][1]))

rect1 = [[1,50],[8,5]]
rect2 = [[-2,-2],[-5,-10]]
print(overlap(rect1,rect2))


#Testing
assert overlap([[1,1],[1,1]],[[2,2],[3,1]]) == 0 #No lines
assert overlap([[1,2],[4,-5]],[[2,2],[3,1]]) == 1 #Rectangle B completely fits inside A
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
assert overlap([[1,50],[8,5]],[[0,5],[3,-10]]) == 0 #Rectangles are not where close to each other
assert overlap([[1,50],[8,5]],[[1,0],[5,-20]]) == 0 #Rectangles are not where close to each other
assert overlap('cat','dog') == 0 #Ensures only a list as the paramters
assert overlap([],[1,2]) == 0 #Ensures no empty lists
assert overlap([],[]) == 0 #Ensures no empty lists
