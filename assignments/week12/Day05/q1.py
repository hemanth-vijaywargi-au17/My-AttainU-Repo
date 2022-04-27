"""
Q-3 ) Top K Frequent Elements (5 marks)
https://leetcode.com/problems/top-k-frequent-elements/
(5 marks)
(Medium)
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

import heapq

class Solution:

    def topKFrequent(self, nums, k):
        
        h =[]
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1     

        for key,val in d.items():

            heapq.heappush(h,(val, key))     
            if len(h) > k:
                heapq.heappop(h)

        return [el[1] for el in h]