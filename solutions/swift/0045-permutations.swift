class Solution {
    func permute(_ nums: [Int]) -> [[Int]] {
        var result: [[Int]] = []
        
        func backtrack(_ nums: [Int], _ path: [Int]) {
            if nums.isEmpty {
                result.append(path)
                return
            }
            for i in 0..<nums.count {
                var newNums = nums
                newNums.remove(at: i)
                backtrack(newNums, path + [nums[i]])
            }
        }
        
        backtrack(nums, [])
        return result
    }
}
