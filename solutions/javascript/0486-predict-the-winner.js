/**
 * @param {number[]} nums
 * @return {boolean}
 */
var PredictTheWinner = function(nums) {
    const n = nums.length;
    const dp = Array.from(Array(n), () => Array(n).fill(0));
    
    for (let i = n-1; i >= 0; --i) {
        for (let j = i; j < n; ++j) {
            if (i == j) {
                dp[i][j] = nums[i];
            } else {
                dp[i][j] = Math.max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1]);
            }
        }
    }
    
    return dp[0][n-1] >= 0;
};
