%Takes a string txt as input and returns another string coded as output

function code = codeit(txt)
    lowerA = 'abcdefghijklmnopqrstuvwxyz';
    capA = upper(lowerA);
    code = '';
    
    %find position in array with char
    %return caps version of positoin in negative
    %horzcat it to answer
    for i = 1:length(txt)
        if int8(txt(i)) >= 65 && int8(txt(i)) <= 90
            %search upper
            pos = strfind(capA,txt(i));
            code = horzcat(code, capA(end - pos + 1));
        elseif int8(txt(i)) >= 97 && int8(txt(i)) <= 122
            %search lower
            pos = strfind(lowerA, txt(i));
            code = horzcat(code, lowerA(end - pos + 1));
        else
            code = horzcat(code, txt(i));
        end
    end
end