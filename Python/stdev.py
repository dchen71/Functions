#Computes standard deviation of a list

def stdev(A):
	#Checks if input is a list
	if not isinstance(A, list):
		return 0

	#Checks to make sure the len is greater than 1
	if len(A) <= 1:
		return 0

print(stdev([]))

assert stdev('cat') == 0
assert stdev([]) == 0
assert stdev([5]) == 0
