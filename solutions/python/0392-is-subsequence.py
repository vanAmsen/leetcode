class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: 
            return True 
        s_pointer = 0 
        t_pointer = 0 
        while t_pointer < len(t): 
            if t[t_pointer] == s[s_pointer]: 
                s_pointer += 1 
                if s_pointer == len(s): 
                    return True 
            t_pointer += 1 
        return False 
                                                                                                                                             
