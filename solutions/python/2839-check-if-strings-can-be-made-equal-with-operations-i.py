class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check if the two strings are already equal 
        if s1 == s2: 
            return True 

        # Check if the sorted versions of s1 and s2 are equal 
        if sorted(s1) != sorted(s2): 
            return False 

        # Compare the sorted characters at odd and even indices 
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2]) 
                                                                                                
