class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array 
        potions.sort() 

        res = [] 
        m = len(potions) 

        for spell in spells: 
            # Find the first potion such that the product of spell and potion is at least success 
            idx = bisect.bisect_left(potions, success // spell + (1 if success % spell != 0 else 0)) 

            # Calculate the number of successful pairs with the current spell 
            res.append(m - idx) 

        return res 
                                                                                                                                      
