public class Solution {
    public bool PredictTheWinner(int[] nums) {
        int n = nums.Length;
        int[,] dp = new int[n, n];
        
        for (int i = n-1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (i == j) {
                    dp[i, j] = nums[i];
                } else {
                    dp[i, j] = Math.Max(nums[i] - dp[i+1, j], nums[j] - dp[i, j-1]);
                }
            }
        }
        
        return dp[0, n-1] >= 0;
    }
}
