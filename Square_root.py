import math


def mySqrt(x: int) -> int:
    return math.floor(math.sqrt(x))


def mySqrt1(x: int) -> int:
    squares = (integer * integer for integer in range(x + 2))
    return next(pair[0] for pair in enumerate(squares) if pair[1] > x) - 1


print(mySqrt(9000000000000000))
print(mySqrt1(9000000000000000))
