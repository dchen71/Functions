#08 Book-Titles TestFirst Ruby

class Book

	def title=(book)
		answer = ""
		lowercase = ['a','an','in','the', 'and', 'of']
  	  
		book.split.each do |word|
  	  		if lowercase.include?word #lower case the less important text
  	  			answer += word.downcase + " "
  	  		else
  	  			answer += word.capitalize + " "
  	  		end
  	  	end
	
	  	answer[0] = answer[0].capitalize #capitalize the first char
	
		@title =  answer[0...-1]
  	end

  	def title
  		@title
  	end

end


