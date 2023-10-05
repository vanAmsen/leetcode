class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # Create a graph representation 
        roads = defaultdict(list) 
        for a, b in connections: 
            roads[a].append((b, True))  # True indicates road from a to b 
            roads[b].append((a, False)) # False indicates road from b to a 

        # Initialize variables 
        self.visited = set()  
        self.count = 0 

        # DFS function 
        def dfs(city): 
            self.visited.add(city) 
            for next_city, direction in roads[city]: 
                if next_city not in self.visited: 
                    if direction: # if road is from current city to next city 
                        self.count += 1 
                    dfs(next_city) 

        dfs(0) 
        return self.count 
                                                                                                                                                                                                                                                      
