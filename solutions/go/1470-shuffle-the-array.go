func shuffle(nums []int, n int) []int {
    // Initialize an array to store the shuffled elements
    shuffled := make([]int, 2 * n)
    
    // Initialize two pointers, one for the first half and the other for the second half
    i, j := 0, n
    
    // Loop through the new array, inserting elements from the two halves of the original array
    for k := 0; k < 2 * n; k += 2 {
        shuffled[k] = nums[i]
        shuffled[k + 1] = nums[j]
        
        // Move the pointers
        i++
        j++
    }
    
    return shuffled
}
