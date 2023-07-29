class Solution {
    public int equalPairs(int[][] grid) {
        // Get grid size 
        int n = grid.length; 
        // Create transposed grid 
        int[][] transpose_grid = new int[n][n]; 
        for (int i = 0; i < n; i++) { 
            for (int j = 0; j < n; j++) { 
                transpose_grid[j][i] = grid[i][j]; 
            } 
        } 
        // Initialize counter for equal row-column pairs 
        int count = 0; 
        for (int i = 0; i < n; i++) { 
            for (int j = 0; j < n; j++) { 
                // Compare i-th row of grid with j-th row of transposed grid 
                if (Arrays.equals(grid[i], transpose_grid[j])) { 
                    // Increment count if pair is equal 
                    count++; 
                } 
            } 
        } 
        // Return total count of equal pairs 
        return count; 
                                          
    }
}
