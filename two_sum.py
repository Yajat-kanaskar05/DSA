'''
Problem - two sum
Problem link - https://leetcode.com/problems/two-sum/description/

Approach - Hashmap (dictionary)

'''




class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        out = []

        dict_d = {}

        for idx,num in enumerate(nums):
            dict_d[num] = idx

        for i,num in enumerate(nums):
            desired = target - num
            if desired in dict_d and dict_d[desired] != i:
                return i,dict_d[desired]