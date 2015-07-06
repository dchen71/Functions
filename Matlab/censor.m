%A function whose first input argument is a cell vector (row or column) of
%strings and whose second input argument is a string. It removes each element of the cell vector 
%whose string is either identical to the second input argument or contains the second argument
%as a substring. The resulting cell vector is returned as the only output argument.

function answer = censor(cv, string)
    sizes = size(cv);
    total = sizes(1) + sizes(2) - 1
    %used to return answer removing string
    %answer = cv;
    answer = cell(0);
    start = true;
    
    for i  = 1:total
        indexes = strfind(cv{i},string);
        indexes = indexes(end:-1:1);
        if isempty(indexes)
            if start
                answer{1,1} = cv{i};
                start = false;
            else
                answer{end + 1,1} = cv{i};
            end
        end
        %To return it sans string in cv
        %for j = 1:length(indexes)
        %    answer{i}(indexes(j):indexes(j) + length(string)) = '';
        %end
    end

end