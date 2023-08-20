class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [ 
            "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) 
            for i in range(1, n+1) 
        ] 
                                                
