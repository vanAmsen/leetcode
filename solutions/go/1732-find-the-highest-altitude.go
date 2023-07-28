func largestAltitude(gain []int) int {
    maxAltitude := 0 
    currentAltitude := 0 

    for _, g := range gain { 
        currentAltitude += g 
        if currentAltitude > maxAltitude { 
            maxAltitude = currentAltitude 
        } 
    } 
    return maxAltitude 
                                                               
}
