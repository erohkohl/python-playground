import time

#def measure_time_of_func(func):

#	def wrapper_func(*agrs, **kwargs)
	
# Returns a list with first n numbers of fibonacci sequence.
def fib(n):
	sequence = [1, 1]
	for i in range(2, n, 1):
		sequence.append(sequence[i - 1] + sequence[i - 2])
	return sequence


