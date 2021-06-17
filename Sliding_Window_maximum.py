import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
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