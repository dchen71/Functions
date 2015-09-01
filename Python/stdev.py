#Computes standard deviation of a list
import statistics
import math

#Class which takes a set of values and returns the standard devation of the values in the list
class stdev(object):
	def __init__(self, values):
		if self.validator(values) != 0:
			self.values = values
			self.sigma = 0
			self.mean = sum(self.values) / len(self.values)
			self.stdev = self.calc_stdev()
		else:
			self.stdev = 0

	#Calculates the standard deviation
	def calc_stdev(self):
		for i in self.values:
			self.sigma += math.pow((i - self.mean),2)
		self.stdev =  math.sqrt(self.sigma / (len(self.values) - 1))

		return self.stdev

	#Logic checker for if the list is a list and if its if its length is greater than 1
	def validator(self, values):
		if not isinstance(values, list):
			return 0
		if len(values) <= 1:
			return 0

	def get_stdev(self):
		return self.stdev

#Tests to ensure that the proper standard deviation is returned
assert stdev('cat').get_stdev() == 0
assert stdev([]).get_stdev() == 0
assert stdev([5]).get_stdev() == 0
assert stdev([1,2]).get_stdev() == statistics.stdev([1,2])
assert stdev([-1,2]).get_stdev() == statistics.stdev([-1,2])
assert stdev([1,2,3,5]).get_stdev() == statistics.stdev([1,2,3,5])
assert stdev([-1,2,-3,5]).get_stdev() == statistics.stdev([-1,2,-3,5])
assert stdev([-1,2.3,-3,5]).get_stdev() == statistics.stdev([-1,2.3,-3,5])