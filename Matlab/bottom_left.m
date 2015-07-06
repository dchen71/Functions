%Returns the n-by-n square array with the bottom left corner of N.  

function N = bottom_left(N,n)
    sizeN = size(N);
    great = sizeN(sizeN > n);
    N = N(end - n + 1 :1:end, 1:1:n);

end