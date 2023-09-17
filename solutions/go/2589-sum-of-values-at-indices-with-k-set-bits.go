func sumIndicesWithKSetBits(nums []int, k int) int {
    sum := 0 

    for i, val := range nums { 
        // Count the set bits for index i 
        setBits := 0 
        index := i 
        for index > 0 { 
            setBits += index & 1 
            index >>= 1 
        } 

        // Add the value at index i if setBits equals k 
        if setBits == k { 
            sum += val 
        } 
    } 

    return sum 
                                                                                                                     
}
