'''
Problem - Contains Duplicate
Problem link - https://leetcode.com/problems/contains-duplicate/description/

Approach - Hashmap (dictionary)
'''



class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        d = {}

        for i,j in enumerate(nums):
            if(j not in d):
                d[j] = i
            else:
                return True
        return False 