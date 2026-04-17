/*

problem - subtract the sum and product of a integer's digits
problem link - https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

*/

class Solution {
public:
    int subtractProductAndSum(int n) {
        int prod = 1;
        int sum = 0;
        int z;

        while(n != 0){

            z = n % 10;
            prod *= z;
            sum += z;

            n = n/10;
        }
        int result = (prod - sum);
        return result;
    }
};