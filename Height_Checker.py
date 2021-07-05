from typing import List

import numpy as np


def heightChecker(self, heights: List[int]) -> int:
    ab = np.array(heights)
    ab.sort()
    return sum(heights != ab)
