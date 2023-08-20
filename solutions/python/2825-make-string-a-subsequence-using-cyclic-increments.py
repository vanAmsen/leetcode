class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0 
        operation_used = False 

        while i < len(str1) and j < len(str2): 
            # If characters match, move both pointers 
            if str1[i] == str2[j]: 
                i += 1 
                j += 1 
            else: 
                # Check if incrementing str1[i] results in a match with str2[j] 
                incremented_char = chr(((ord(str1[i]) - ord('a') + 1) % 26) + ord('a')) 
                if incremented_char == str2[j] and not operation_used: 
                    # Move both pointers 
                    i += 1 
                    j += 1 
                else: 
                    # Move only the pointer i 
                    i += 1 
                    # Mark operation as used if we've incremented a character 
                    if incremented_char == str2[j]: 
                        operation_used = True 

        # Return True if we've gone through all of str2 
        return j == len(str2) 
