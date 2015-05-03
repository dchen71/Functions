#Finds the largest prime factor from an input number
'''
#Tests if a number is prime
def primetest(n):
	for i in range(2,n):
		if(n % i == 0):
			return False
	return True
'''
#Determines the largest prime factor in a number
def primetest(x):
	
	if x < 2:
		return x
	
	prime = 2;
	while(x > prime):
		#if evenly divisble, can shrink it down more since not prime
		if(x % prime == 0):
			x = x/prime
			prime = 2 #resets so it can redetermine the largest prime since the common divisors are down here
		else:
			prime += 1
	return prime

print(primetest(600851475143))