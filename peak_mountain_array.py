'''
problem - peak index in a mountain array
problem link - https://leetcode.com/problems/peak-index-in-a-mountain-array/
'''

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        
        s = 0
        e = len(arr) - 1

        while s < e:
            mid = s + (e - s) // 2
            if arr[mid] < arr[mid + 1]:
                s = mid + 1
            else:
                e = mid

        return s