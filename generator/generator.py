from time import sleep


# Returns a list with first n numbers of fibonacci sequence as generator.
def fib(n):
    sequence = [1, 1]
    for i in range(0, n, 1):
        sleep(.5)
        if i == 0:
            yield 1
        elif i == 1:
            yield 1
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
            yield sequence[i - 1] + sequence[i - 2]
