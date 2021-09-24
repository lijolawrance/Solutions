from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_number = 0
        left, right = 0, len(people) - 1
        print(left, right, people)
        while left <= right:
            if left == right:
                boat_number += 1
                break
            print(people[left], people[right])
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boat_number += 1
            print(boat_number, right, left)

        return boat_number


soln = Solution()
print(soln.numRescueBoats([1, 1, 2, 3, 3], 3))
