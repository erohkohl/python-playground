import decorator as Decorator


def test_fib():
    result = Decorator.fib(10)
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 51]
    assert expected == result
