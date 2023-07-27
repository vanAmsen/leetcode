/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let window_sum = 0;
    for (let i = 0; i < k; i++) {
        window_sum += nums[i];
    }
    let max_avg = window_sum / k;

    for (let i = k; i < nums.length; i++) {
        window_sum += nums[i] - nums[i - k];
        max_avg = Math.max(max_avg, window_sum / k);
    }
    return max_avg;    
};
