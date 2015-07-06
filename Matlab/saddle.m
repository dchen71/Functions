%Finds the saddle point which is an element whose value is greater than or equal to every element in its
%row, and less than or equal to every element in its column.

function point =  saddle(M)
    point = zeros(0);
    dim = size(M);
    col = dim(1);
    row = dim(2);

    for i = 1:row
       for j = 1:col
          if M(j,i) == max(M(j, 1:row))
              if M(j,i) == min(M(1:col,i))
                 point(end + 1,1) = j;
                 point(end,2) = i;
              end
          end
       end
    end

end