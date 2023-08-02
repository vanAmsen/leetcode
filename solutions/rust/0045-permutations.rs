impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        Self::backtrack(nums, vec![], &mut result);
        result
    }

    fn backtrack(nums: Vec<i32>, path: Vec<i32>, result: &mut Vec<Vec<i32>>) {
        if nums.is_empty() {
            result.push(path);
            return;
        }
        for i in 0..nums.len() {
            let mut new_nums = nums.clone();
            new_nums.remove(i);
            let mut new_path = path.clone();
            new_path.push(nums[i]);
            Self::backtrack(new_nums, new_path, result);
        }
    }
}
