import decorator as Decorator


def test_fib():
    (result, _) = Decorator.fib(10)
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    assert expected == result


def test_fib_time():
    (_, time) = Decorator.fib(10)

    assert time > 0
