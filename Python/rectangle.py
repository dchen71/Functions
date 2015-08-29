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

    #Tests whether or not the rectangles overlap and computes the overlap area
    #Will only work on non-directional rectangles
    if A_x1 <= B_x1 & B_x1 <= A_x2:
        print('woo')
        if A_y1 >= B_y1 & B_y1 >= A_y2: #Top of B fits in
            print('cow')
            if B_y2 >= A_y2 & B_y2 < A_y1: #Assuming rectangle B completely fits inside
                print('meow')
                overlap = area(B)
            elif B_y2 <= A_y2: #Assuming x coords fit inside but y at bottom juts out
                print('coo')
                overlap = area([[B_x1,B_y1],[B_x2,A_x2]])
            else:
                print('mm')
        elif A[0][1] >= B[0][1] & B[0][1] >= A[1][1]:
            print('tbda')
        else:
            print('tgbb')
    else:
        print('tbd')


    return (overlap)

def area(A):
    return abs((A[0][0] - A[1][0]) * (A[0][1] - A[1][1]))

rect1 = [[1,2],[4,-5]]
rect2 = [[2,2],[3,1]]
print(overlap(rect1,rect2))


#Testing
assert overlap([[1,2],[4,-5]],[[2,2],[3,1]]) == 1 #Rectangle B completely fits inside A
assert overlap([[1,2],[4,-5]],[[2,2],[3,-4]]) == 6 #Rectangle B stretches inside A
assert overlap([[1,2],[4,-5]],[[2,2],[3,3]]) == 0 #Rectangle B touchs but is not in A
assert overlap('cat','dog') == 0 #Ensures only a list as the paramters
assert overlap([],[1,2]) == 0 #Ensures no empty lists
assert overlap([],[]) == 0 #Ensures no empty lists
