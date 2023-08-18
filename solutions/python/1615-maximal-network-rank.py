class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Compute the degree for each city
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        # Using a set to store the roads for O(1) lookup
        road_set = set(tuple(road) for road in roads)
        
        max_rank = 0
        # Step 2: Iterate over all pairs of cities
        for i in range(n):
            for j in range(i+1, n):
                # Calculate network rank
                rank = degree[i] + degree[j]
                
                # If there's a direct road between i and j, subtract 1
                if (i, j) in road_set or (j, i) in road_set:
                    rank -= 1
                
                # Step 3: Keep track of the maximal network rank
                max_rank = max(max_rank, rank)
                
        return max_rank
