func rob(nums []int) int {
    n := len(nums) 
    if n == 0 { 
        return 0 
    } 
    if n == 1 { 
        return nums[0] 
    } 

    // Initialize a dynamic programming array to keep track of the maximum amount 
    // of money that can be robbed up to each house 
    dp := make([]int, n) 

    // Base cases 
    dp[0] = nums[0] 
    dp[1] = max(nums[0], nums[1]) 

    // Iterate through the houses, calculating the maximum amount of money 
    // that can be robbed up to each one 
    for i := 2; i < n; i++ { 
        dp[i] = max(dp[i-1], dp[i-2]+nums[i]) 
    } 

    return dp[n-1] 
                                                                                                     
}

// Helper function to return the maximum of two integers 
func max(a, b int) int { 
    if a > b { 
            return a 
    } 
    return b 
} 
                
