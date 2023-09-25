class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize the tower with all glasses empty 
        tower = [[0] * 100 for _ in range(100)] 

        # Pour the champagne into the top glass 
        tower[0][0] = poured 

        # Go through each glass and distribute the overflow 
        for row in range(query_row + 1):  
            for col in range(row + 1):   
                overflow = (tower[row][col] - 1) / 2   
                if overflow > 0:   
                    if row < 99:   
                        tower[row + 1][col] += overflow  
                        tower[row + 1][col + 1] += overflow   

        # Return the amount in the queried glass, capped at 1 
        return min(1, tower[query_row][query_glass]) 
                                                                                                                                                                                                                  
