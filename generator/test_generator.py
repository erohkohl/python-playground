import generator as Generator


def test_fib():
    result = Generator.fib(10)
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    for (i, j) in zip(expected, result):
        assert i == j
