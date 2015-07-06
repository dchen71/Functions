%Takes the name of a text file as input and returns the
%number of letters (i.e., any of the characters, a-to-z and A-to-Z) that the file contains.

function numLetters = letter_counter(input1)
    numLetters = 0;
    fid = fopen(input1,'rt');
    
    %Checks if error opening file
    if fid < 0
        numLetters = -1;
        return;
    end
    
    %Reads the data
    oneline = fgets(fid);
    while ischar(oneline)
        dim = length(oneline);
        for i = 1:dim
            if isletter(oneline(i))
                numLetters = numLetters + 1;
            end
        end
        oneline=fgets(fid);
    end
    
    fclose(fid);
end