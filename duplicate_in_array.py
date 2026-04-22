'''
problem - finad all duplicates in array
problem link - https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        
        result = []
        for x in nums:
            idx = abs(x) - 1          

            if nums[idx] < 0:         
                result.append(idx + 1)
            else:
                nums[idx] = -nums[idx] 

        return result