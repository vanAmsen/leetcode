/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function(nums) {
    let n = nums.length;
    let distinct_elements = new Set(nums).size;
    let count = 0;
    let left = 0;
    let right = 0;
    let counter = new Map();

    while (right < n) {
        counter.set(nums[right], (counter.get(nums[right]) || 0) + 1);
        while (counter.size === distinct_elements) {
            counter.set(nums[left], counter.get(nums[left]) - 1);
            if (counter.get(nums[left]) === 0) {
                counter.delete(nums[left]);
            }
            left++;
            count += n - right;
        }
        right++;
    }
    return count;    
};
