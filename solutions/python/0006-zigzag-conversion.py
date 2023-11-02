class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1 or s has less than numRows characters, return s as is 
        if numRows == 1 or numRows >= len(s): 
            return s 

        # Create a list of strings for each row 
        rows = [""] * numRows 

        # Initialize currentRow and direction 
        currentRow = 0 
        direction = -1  # 1 for downwards, -1 for upwards 

        # Iterate through each character in s 
        for char in s: 
            # Add the character to the current row 
            rows[currentRow] += char 

            # If we're at the top or bottom row, change direction 
            if currentRow == 0 or currentRow == numRows - 1: 
                direction *= -1 

            # Move to the next row in the current direction 
            currentRow += direction 

        # Concatenate all the strings in rows to get the final zigzag string 
        return ''.join(rows) 
                                                                                                                                                                                                                                                     
