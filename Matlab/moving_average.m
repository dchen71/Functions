
% Finds the average of a vector of max 25 elements
function average = moving_average(x)
    persistent aver;
    [n,m] = size(aver);
    
    if m == 0
        aver(1,1) = x;
        average = x;
    end
    
    if m < 25 && m ~= 0
        aver(n,m +1) = x;
    elseif m == 25
        aver(1,1) = x;
        aver = circshift(aver,-1,2);
    end
    
    average = mean(aver);
    
end