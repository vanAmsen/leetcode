public class Solution {
    public void permuteRec(int[] nums, int begin, List<List<Integer>> result) {
        if (begin == nums.length) {
            List<Integer> temp = new ArrayList<Integer>();
            for (int num : nums) temp.add(num);
            result.add(temp);
            return;
        }
        for (int i = begin; i < nums.length; i++) {
            // Swap
            int temp = nums[begin];
            nums[begin] = nums[i];
            nums[i] = temp;
            
            permuteRec(nums, begin + 1, result);
            
            // Swap back
            temp = nums[begin];
            nums[begin] = nums[i];
            nums[i] = temp;
        }
    }
    
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        permuteRec(nums, 0, result);
        return result;
    }
}
