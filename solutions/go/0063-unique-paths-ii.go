func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    if len(obstacleGrid) == 0 || len(obstacleGrid[0]) == 0 || obstacleGrid[0][0] == 1 {
        return 0
    }

    m := len(obstacleGrid)
    n := len(obstacleGrid[0])

    previous := make([]int, n)
    current := make([]int, n)
    previous[0] = 1

    for i := 0; i < m; i++ {
        if obstacleGrid[i][0] == 1 {
            current[0] = 0
        } else {
            current[0] = previous[0]
        }
        
        for j := 1; j < n; j++ {
            if obstacleGrid[i][j] == 1 {
                current[j] = 0
            } else {
                current[j] = current[j-1] + previous[j]
            }
        }
        previous, current = current, previous
    }
    return previous[n-1]
}
