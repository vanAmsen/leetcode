class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # Defining our MOD constant 
        MOD = 10**9 + 7 

       # Initialize counts for all vowels for n = 1 
        a, e, i, o, u = 1, 1, 1, 1, 1 

        # Update counts based on the transitions 
        for _ in range(1, n): 
            a_next = e 
            e_next = (a + i) % MOD 
            i_next = (a + e + o + u) % MOD 
            o_next = (i + u) % MOD 
            u_next = a 

            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next 

        return (a + e + i + o + u) % MOD 
                                                                                                                                                                  
