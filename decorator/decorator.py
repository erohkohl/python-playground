import time

# Decorator
def measure_time_of_func(func):
    def wrapper_func(n):
        start_time = time.time()
        fib_seq = func(n)
        end_time = time.time()
        return (fib_seq, end_time - start_time)
    return wrapper_func


# Returns a list with first n numbers of fibonacci sequence.
@measure_time_of_func
def fib(n):
    sequence = [1, 1]
    for i in range(2, n, 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence
