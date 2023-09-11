func findMinArrowShots(points [][]int) int {
	// Step 1: Sort the points by their ending coordinate 
	sort.Slice(points, func(i, j int) bool { 
			return points[i][1] < points[j][1] 
	}) 

	// Step 2: Initialize variables 
	arrows := 0 
	end := math.MinInt64  
	// Initialize to smallest possible integer value 

	// Step 3: Loop through the sorted points 
	for _, point := range points { 
		if point[0] > end { 
			// Shoot a new arrow 
			arrows++ 
			end = point[1] 
		} 
	} 

	return arrows 
												
}
