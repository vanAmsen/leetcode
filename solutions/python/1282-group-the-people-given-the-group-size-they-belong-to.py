class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        current_groups = {}
        
        for i, size in enumerate(groupSizes):
            if size not in current_groups:
                current_groups[size] = []
                
            current_groups[size].append(i)
            
            if len(current_groups[size]) == size:
                result.append(current_groups[size])
                current_groups[size] = []
                
        return result
