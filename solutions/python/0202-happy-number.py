class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n): 
            return sum(int(i)**2 for i in str(n)) 

        seen = set() 
        while n != 1 and n not in seen: 
            seen.add(n) 
            n = get_next(n) 

        return n == 1 
                                                                                                 
