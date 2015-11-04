#Converts numbers to words from 0-999

def number_to_words(number)
  #Only works for numbers between 0 and 999999
  if number >= 0 && number  < 1000000
  	#Last digit at the end
  	sixth = number.to_s[number.to_s.length - 1]

  	#Dictionaries containing the word values/values
  	single_dict = {'0' => 'zero','1'=>'one', '2'=>'two', '3'=>'three', '4'=> 'four', '5'=>'five', '6'=> 'six', '7'=>'seven', '8'=>'eight', '9'=>'nine'}
  	tens_dict = {'1'=>'ten', '2'=> 'twenty', '3'=>'thirty', '4'=>'forty', '5'=>'fifty', '6'=>'sixty', '7'=>'seventy', '8'=>'eighty', '9'=>'ninety'}
  

  	if number.to_s.length == 1 #Single digit
  		word = single_dict[sixth]
  	elsif number.to_s.length >= 2 #Begins building sequence of word based on length starting with 2
  		fifth = number.to_s[number.to_s.length - 2]
  		if sixth == '0'
  			word = "#{tens_dict[fifth]}"
  		elsif fifth != '0'
  			word = "#{tens_dict[fifth]}-#{single_dict[sixth]}"
  		else
  			word = "#{single_dict[sixth]}"
  		end
  		if number.to_s.length >= 3 #Continues to build sequence based on hundreds
			fourth = number.to_s[number.to_s.length - 3]
			if fourth != '0'
				if fifth == '0'
					if sixth ==  '0'
						word = "#{single_dict[fourth]} hundred"
					end
				else 
					word = "#{single_dict[fourth]} hundred and " + word
				end
			end
  			if number.to_s.length >= 4 #Continues to build based on thousands
  				third = number.to_s[number.to_s.length - 4]
				if third != '0'
					if fourth == '0' && fifth == '0'
						if sixth != '0'
							word = "#{single_dict[third]} thousand and " + word
						else
							word = "#{single_dict[third]} thousand"
						end
					else 
						word = "#{single_dict[third]} thousand " + word
					end
				end
  				if number.to_s.length >= 5 #Continues to build based on tens of thousands
  					second = number.to_s[number.to_s.length - 5]
  					if second != '0'
  						if third != '0'
  							word = "#{tens_dict[second]}-" + word
  						else
  							if fourth == '0' && fifth == '0' && sixth == '0'
  								word = "#{tens_dict[second]} thousand"
  							else
  								word = "#{tens_dict[second]} thousand " + word
  							end
  						end
					elsif
						if third != '0'
							if fourth == '0' && fifth == '0' && sixth == '0'
								word = "#{tens_dict[second]} thousand"
  							else
  								word = "#{tens_dict[second]} thousand " + word
  							end
  						end
  					end
  						if number.to_s.length == 6 #Builds the sequences of those hundreds of thousands
  							first = number.to_s[0]
  							if second == '0' && third == '0' && fourth == '0' && fifth == '0'
  								if sixth == '0'
  									word = "#{single_dict[first]} hundred thousand"
  								else
  									word = "#{single_dict[first]} hundred thousand and " + word
  								end
  							else
  								word = "#{single_dict[first]} hundred and " + word
  							end
						end
  					end
  				end
  			end
  		end
  else
  	word = "not in range"
  end
  word
end