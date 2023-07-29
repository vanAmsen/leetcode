public class Solution {
    public int EqualPairs(int[][] grid) {
        // Get grid size
        int n = grid.Length;
        // Create transposed grid
        int[][] transposeGrid = new int[n][];
        for (int i = 0; i < n; i++) {
            transposeGrid[i] = new int[n];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                transposeGrid[j][i] = grid[i][j];
            }
        }
        // Initialize counter for equal row-column pairs
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Compare i-th row of grid with j-th row of transposed grid
                if (Enumerable.SequenceEqual(grid[i], transposeGrid[j])) {
                    // Increment count if pair is equal
                    count++;
                }
            }
        }
        // Return total count of equal pairs
        return count;
    }
}
