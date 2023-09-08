func containsNearbyDuplicate(nums []int, k int) bool {
    // Create a map to store the last index of each number 
    numIndex := make(map[int]int) 

    for i, num := range nums { 
        // Check if the number already exists in the map 
        if lastIndex, exists := numIndex[num]; exists { 
            // Check if the distance between the current index and the last index is <= k 
            if i-lastIndex <= k { 
                return true 
            } 
        } 

        // Update the last index for the current number 
        numIndex[num] = i 
    } 

    return false 
                                                                                                                  
}
