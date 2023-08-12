impl Solution {
    pub fn unique_paths_with_obstacles(obstacleGrid: Vec<Vec<i32>>) -> i32 {
        if obstacleGrid.is_empty() || obstacleGrid[0].is_empty() || obstacleGrid[0][0] == 1 { 
            return 0; 
        } 

        let m = obstacleGrid.len(); 
        let n = obstacleGrid[0].len(); 

        let mut previous = vec![0; n]; 
        let mut current = vec![0; n]; 
        previous[0] = 1; 

        for row in &obstacleGrid { 
            current[0] = if row[0] == 1 { 0 } else { previous[0] }; 
            for j in 1..n { 
                if row[j] == 1 { 
                    current[j] = 0; 
                } else { 
                    current[j] = current[j-1] + previous[j]; 
                } 
            } 
            std::mem::swap(&mut previous, &mut current); 
        } 

        previous[n-1] 
                                                                                                                                                                                                                                                                            
    }
}
