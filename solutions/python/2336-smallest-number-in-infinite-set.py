class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1   
        self.added = set()  
                      

    def popSmallest(self) -> int:
        # If the set of added back numbers is not empty, pop the smallest number from it 
        if self.added: 
            res = min(self.added) 
            self.added.remove(res) 
            return res 
        # Otherwise, return the current counter value and increment it 
        res = self.cur 
        self.cur += 1 
        return res 
                                                                                       

    def addBack(self, num: int) -> None:
        # Only add the number back if it's smaller than the current counter value 
        if num < self.cur: 
            self.added.add(num) 
                                     


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
