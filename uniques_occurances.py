"""
problem - unique number of occurances 
problem link - https://leetcode.com/problems/unique-number-of-occurrences/description/
"""

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        d = {}

        for i in range(0,len(arr)):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1

        s = set(d.values())
        if(len(d.values()) == len(s)):
            return True
        else:
            return False