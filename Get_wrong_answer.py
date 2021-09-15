def getWrongAnswers(N: int, C: str) -> str:
    return (C.replace('A', 'b').replace('B', 'a')).swapcase()


print(getWrongAnswers(3, 'ABA'))
