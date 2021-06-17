from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        flowers = [0] * n
        garden = defaultdict(list)
        for src, dst in paths:
            garden[src].append(dst)
            garden[dst].append(src)
        for i in range(1, n + 1):
            colors = {1, 2, 3, 4}
            var = {colors.remove(flowers[neigh - 1]) for neigh in garden[i] if flowers[neigh - 1] in colors}
            flowers[i - 1] = colors.pop()
        return flowers
