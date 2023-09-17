func minimumRightShifts(nums []int) int {
    n := len(nums) 
    pivotCount := 0 
    pivotIndex := -1 

    // Step 1: Finding the Pivot Point 
    for i := 0; i < n; i++ { 
        if nums[i] > nums[(i+1)%n] { 
            pivotCount++ 
            pivotIndex = i 
        } 
    } 

    // Step 2: Check for Multiple Pivot Points 
    if pivotCount > 1 { 
        return -1 
    } 

    // Step 3: Calculate Right Shifts 
    if pivotCount == 1 { 
        return n - (pivotIndex + 1) 
    } 

    // If the array is already sorted 
    return 0 
                                                                                                                
}
