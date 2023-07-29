class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = Counter(arr) 
        count_values = list(count_dict.values()) 
        return len(count_values) == len(set(count_values)) 
                             
