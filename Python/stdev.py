#Computes standard deviation of a list
import statistics
import math

def stdev(A):
	#Checks if input is a list
	if not isinstance(A, list):
		return 0

	#Checks to make sure the len is greater than 1
	if len(A) <= 1:
		return 0

	mean = sum(A) / len(A)
	sigma = 0
	for i in A:
		sigma += math.pow((i - mean),2)
	return math.sqrt(sigma / (len(A) - 1))

#Tests to ensure that the proper standard deviation is returned
assert stdev('cat') == 0
assert stdev([]) == 0
assert stdev([5]) == 0
assert stdev([1,2]) == statistics.stdev([1,2])
assert stdev([-1,2]) == statistics.stdev([-1,2])
assert stdev([1,2,3,5]) == statistics.stdev([1,2,3,5])
assert stdev([-1,2,-3,5]) == statistics.stdev([-1,2,-3,5])
assert stdev([-1,2.3,-3,5]) == statistics.stdev([-1,2.3,-3,5])