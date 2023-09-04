class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Counter for symmetric integers 
        count = 0  

        for num in range(low, high + 1): 
            # Convert the integer to a string to easily access its digits 
            str_num = str(num)   
            # Number of digits in the integer 
            n = len(str_num)   

            # Skip numbers with an odd number of digits 
            if n % 2 != 0: 
                continue 

            # Calculate the sum of the first half and second half of the digits 
            first_half_sum = sum(int(digit) for digit in str_num[:n // 2]) 
            second_half_sum = sum(int(digit) for digit in str_num[n // 2:]) 

            # Check if the integer is symmetric 
            if first_half_sum == second_half_sum: 
                count += 1 

        return count 
                                                                                                                                                                                                                                                                   
