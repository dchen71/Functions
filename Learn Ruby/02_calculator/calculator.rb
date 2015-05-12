#Lesson 2 - Calculator TestFirst.org learn ruby

#Adds two numbers together
def add(num1,num2)
	return num1 + num2
end

#Subtracts 2 numbers
def subtract(num1, num2)
	return num1 - num2
end

#Computes the sum of the array
def sum(array)
	total = 0
	for number in array #could do each do instead of for loop
		total += number
	end
	return total
end

#Multiplies 2 numbers
def multiply(num1, num2)
	return num1 * num2
end

def power(num1, power)
	return num1**power
end

#Computes factorial
def factorial(num)
	total = 0
	(1..num).each do |i|
		if i == 1
			total = 1
		else
			total *= i
		end
	end
	return total
end
