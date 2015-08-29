#Finds the area of overlapping rectangles given array of points

def overlap(A,B):
    area_A = 0
    area_B = 0
    overlap = 0

    #Validate that each point has 2 vertices
    if len(A) < 2 | len(B) < 2:
        return overlap
    else:    
        if len(A[0]) < 2 | len(A[1]) < 2 | len(B[0]) < 2 | len(B[0]) < 2:
            return overlap

    #Validate that each diagonal makes a rectange(diagonal points arent equal)
    if A[0][0] == A[1][0] | A[0][1] == A[1][1] | B[0][0] == B[1][0] | B[0][1] == B[1][1]:
        return overlap
    
    #Computes the areas of each rectangle
    area_A = abs((A[0][0] - A[1][0]) * (A[0][1] - A[1][1]))
    area_B = abs((B[0][0] - B[1][0]) * (B[0][1] - B[1][1]))
    

    #Tests whether or not the rectangles overlap and computes the overlap area
    


    return overlap

rect1 = [[1,2],[4,-5]]
rect2 = [[2,2],[3,1]]
print(overlap(rect1,rect2))


#Testing
#assert overlap([[1,2],[4,-5]],[[2,2],[3,1]]) == 20