def numJewelsInStones(jewels: str, stones: str) -> int:
    return sum(map(stones.count, list(jewels)))


class Solution:
    pass
