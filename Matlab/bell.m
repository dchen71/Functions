% Returns the first n rows of the Bell triangle, where n is an input argument

function B = bell(n)
    integerTest =~mod(n,1);

    if n <= 0 || integerTest == 0
        B = zeros(0);
    else
        B(1,1) = 1;
        for i=2:n
            B(i,1) = B(1,end);
            for j = 1:i-1
                B(i-j,j+1) = B(i-j+1,j)+B(i-j,j);
            end
        end
    end
end