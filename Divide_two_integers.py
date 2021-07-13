
def divide(dividend: int, divisor: int) -> int:
    MAX_VALUE = 2 ** 31
    div = int(dividend / divisor)
    if div >= MAX_VALUE:
        return MAX_VALUE-1
    elif div < -1 * MAX_VALUE:
        return -1 * MAX_VALUE
    return div


# print(divide(1,1))
print(divide(7, -3))
print(divide(-2147483648, -1))
print(divide(-2147483648, 1))
print(divide(2147483647, 2))
print(divide(-2147483648, -3))
