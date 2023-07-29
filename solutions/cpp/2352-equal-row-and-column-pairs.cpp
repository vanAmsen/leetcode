class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
            // Get grid size  
        int n = grid.size();  
        // Create transposed grid  
        vector<vector<int>> transpose_grid(n, vector<int>(n));  
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
                if (grid[i] == transpose_grid[j]) {  
                    // Increment count if pair is equal  
                    count++;  
                }  
            }  
        }  
        // Return total count of equal pairs  
        return count;  
    } 
}; 
                                                                                                                                                                                                                                                            
