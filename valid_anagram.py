"""
problem - Valid Anagram
problem link - https://leetcode.com/problems/valid-anagram/

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_sort = sorted(s)
        t_sort = sorted(t)

        if(s_sort == t_sort):
            return True
        else:
            return False
            