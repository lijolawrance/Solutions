from collections import Counter

def numIdenticalPairs(self, nums: List[int]) -> int:
    return sum(num * (num - 1) for num in Counter(nums).values() if num > 1) // 2




'''
We are asked to return the total number of pairs in a list of numbers (pair (i,j) is called good if nums[i] == nums[j] and i < j).

First, let's consider a list of just one number, e.g. nums = [1]. Here, this number cannot be paired with any others (other than itself), so the result is zero.

Next, let's consider a list of all idential numbers, e.g. nums = [1, 1, 1, 1]. What we are really being asked is how many combinations of two can be made from such a list. Using zero based indexing, we have the following six pairs of such combinations:

(0, 1), (0, 2), (0, 3)  # The first number at index 0 can be paired with the others at index locations 1, 2 and 3.
        (1, 2), (1, 3)  # The second at index 1 can be paired with its matching pair at index locations 2 and 3.
		        (2, 3)  # The third at index 2 can form a unique pair with the number at index location 3.
More generally, the combination formula is n! / [k! * (n - k)!]. In this problem, n represents the count of a given number and k=2 because we are looking at unique pairs. So the general formula becomes n! / [2 * (n - 2)!]. Noting that n! / (n - 2)! is simply n * (n - 1) after cancelling the factorial terms, the total number of unique pairs of the same number can be calculated as n * (n - 1) / 2.

Now let's say we are given the following ten mixed numbers:
nums = [1, 2, 3, 1, 3, 2, 2, 4, 2, 3]

The first thing we want to do is count the number of occurrences of each number, so number: count of number

1: 2
2: 4
3: 3
4: 1
Note that when n = 1, then n * (n - 1) / 2 is simply zero and can hence be ignored (one item cannot be paired with any matching item).

So, the result is as follows given the above set of ten numbers with their respective counts:

1: 2 -> 2 * (2 - 1) / 2 = 1
2: 4 -> 4 * (4 - 1) / 2 = 6
3: 3 -> 3 * (3 - 1) / 2 = 3
4: 1 -> 1 * (1 - 1) / 2 = 0
The answer in this example is thus 1 + 6 + 3 = 10.

Python Implementations

Note that all of this can be solved simply in python using Counter and using a generator expression to sum the calculations for each counted value. Note that n * (n - 1) always results in an even number because it is the product of an odd number and an even number. We can therefore use floor division on the summed result because this summed result will be even. All intermediate results are guaranteed to be integers as is the final result. Note that summing everything and then dividing by two just once is slightly more efficient that summing all intermediate n * (n - 1) / 2 calculations.

from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(num * (num - 1) for num in Counter(nums).values()) // 2
An alternative solution that just uses one pass (O(n) time complexity) to calculated the total pairs:

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        counts = {}
        for num in nums:
            prior_num_count = counts.get(num, 0)
            pairs += prior_num_count
            counts[num] = prior_num_count + 1
        return pairs
By observing the cumulative count, one notes that it is equal to the sum of the prior counts plus one minus the current total count (i.e. the prior count). The solution immediately above uses this obvservation, increasing the pairs count by one less than the number of occurrences observed for each number. This solution has the same O(n) space complexity as the prior solution, as they both require the use of a dictionary/hashmap to keep track of the counts for each number observed.

count: sum of prior counts + (count - 1)
1: 0
2: 1 (0 + 1)
3: 3 (1 + 2)
4: 6 (3 + 3)
5: 10 (6 + 4)
'''