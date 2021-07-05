import itertools.permutations as permutations


def numTilePossibilities(tiles: str) -> int:
    return len({x for i in range(1, len(tiles) + 1) for x in permutations(tiles, i)})


class Solution:
    pass
