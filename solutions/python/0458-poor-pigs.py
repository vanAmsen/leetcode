class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        k = minutesToTest // minutesToDie + 1
        pigs = 1
        while k ** pigs < buckets:
            pigs += 1
        return pigs
