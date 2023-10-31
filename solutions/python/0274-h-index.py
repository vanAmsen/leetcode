class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) 

        for i, c in enumerate(citations): 
            if i >= c: 
                return i 
        return len(citations) 
                                                                       
