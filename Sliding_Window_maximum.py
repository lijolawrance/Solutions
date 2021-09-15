import collections

from typing import List


def maxSlidingWindow_1(nums: List[int], k: int) -> List[int]:
    double_ended = collections.deque(nums)
    max_list = []
    while len(double_ended) >= k:
        maxvalue = double_ended[0]
        for num in range(0, k):
            if double_ended[num] > maxvalue:
                maxvalue = double_ended[num]
        double_ended.popleft()
        max_list.append(maxvalue)
    return max_list


def maxSlidingWindow_2(nums: List[int], k: int) -> List[int]:
    q, res = collections.deque(), []
    for i in range(len(nums)):
        if i - k >= 0:
            res.append(nums[q[0]])
            while q and q[0] <= i - k:
                q.popleft()
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)
    res.append(nums[q[0]])
    return res


def maxSlidingWindow_3(nums: List[int], k: int) -> List[int]:
    return nums and [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


class Solution:
    pass


'''class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            #print ('{} {} {}'.format(k,i,len(nums)))
            if(len(nums) >= k):
                a.append(max(nums[i:k]))
                k=k+1              
        return a'''
'''
[1,3,-1,-3,5,3,6,7]
3
'''
