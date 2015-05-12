#Lesson 04 Pig Latin Test Ruby

def translate(string)
  array = []
  vowels = ['a','e','i','o','u', 'qu']

  string.split.each do |word|
    if vowels.include?word[0]
       append = word + 'ay'
       array.push(append)
    else
      #Checks the consonants
      if word[0..2] == 'sch'
        puts 'qoo'
        append = word + word[0..2]
        append[0..2] = ''
      elsif word[0..1] == 'qu'
        append = word + word[0..1]
        append[0..1] = ''  
      else
        append = word
      end
        
      while(!vowels.include?append[0] and 'qu' != append[0..1])
        if append[1..2] == 'qu'
          append += append[0..2]
          append[0..2] = ''
        else
          append += append[0]
          append[0] = ''
        end
      end
      
      append += 'ay'
      array.push(append)
    end
  end

  answer = ""

  array.each do |word|
    answer += word + " "
  end

  return answer[0...-1]
end



puts translate("dog")