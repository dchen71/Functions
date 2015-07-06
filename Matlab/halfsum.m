%Takes as input at most two dimensional matrix A and
%computes the sum of the elements of A that are in the diagonal or are to the right of it.


function answer =  halfsum(A)
    %sum of values that are row=col and right of ex 3x3 1:9  = 26
    answer = 0;
    dim = size(A);
    
    for col = (1:dim(1))
        for row = (1:dim(2))
            if row >= col
                answer = A(col, row) + answer;
            end
        end
    end
    
end