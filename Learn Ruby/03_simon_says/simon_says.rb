#Lesson 3 - Simon Says TestFirst.org learn ruby

#Echos back the word
def echo(word)
	return word
end

#Returns the word in in upper case
def shout(word)
	return word.upcase
end

#Repeats the word 1-n times
def repeat(word, n = 2)
	return ((word + " ")* n)[0...-1]
end

#Returns the first n letters
def start_of_word(word, n)
	return word[0..(n - 1)]
end

#Returns the first word in a string
def first_word(word)
	return word.split[0]
end

#Capitalizies the first letter
def titleize(word)
	parse = ""
	little = ['the', 'and', 'over']
	
	#Seems inefficient but breaks up and capitalizes and sets the words in a string
	word.split.each do |i|
		if little.include?(i)
			parse += i.downcase + " "
		else
			parse += i.capitalize + " "
		end
	end

	parse[0] = parse[0].upcase #Manually upcases the 1st char
	return parse[0...-1]
end