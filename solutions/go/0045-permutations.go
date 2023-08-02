func permute(nums []int) [][]int {
    var result [][]int
    
    var backtrack func([]int, []int)
    backtrack = func(nums []int, path []int) {
        if len(nums) == 0 {
            result = append(result, append([]int(nil), path...))
            return
        }
        for i := 0; i < len(nums); i++ {
            newNums := append([]int(nil), nums[:i]...)
            newNums = append(newNums, nums[i+1:]...)
            newPath := append([]int(nil), path...)
            newPath = append(newPath, nums[i])
            backtrack(newNums, newPath)
        }
    }
    
    backtrack(nums, []int{})
    return result
}
