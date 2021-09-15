from typing import List


# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    return sum(map(sum, G))/(R*C)


print(getHitProbability(2, 2, [[1, 1], [1, 1]]))
