class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7 
        # Initialize base cases 
        T, T_up, T_down = 1, 0, 0 
        T_prev, T_up_prev, T_down_prev = 1, 0, 0 
        # Values for i-2 
        T_prev2, T_up_prev2, T_down_prev2 = 1, 0, 0 

        # Populate the DP variables 
        for i in range(2, n+1): 
            # Store old values for shifting 
            T_prev2, T_up_prev2, T_down_prev2 = T_prev, T_up_prev, T_down_prev 
            T_prev, T_up_prev, T_down_prev = T, T_up, T_down 

            # Calculate new values 
            T = (T_prev + T_prev2 + T_up_prev + T_down_prev) % MOD 
            T_up = (T_down_prev + T_prev2) % MOD 
            T_down = (T_up_prev + T_prev2) % MOD 

        return T 
                                                                                                                                                                                
