"""
problem - subtract the product and sum of digits of an integer
problem link - https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod = 1
        summ = 0

        while (n != 0):
            z = n % 10

            prod *= z
            summ += z

            n = n//10
        
        result = prod - summ
        return result