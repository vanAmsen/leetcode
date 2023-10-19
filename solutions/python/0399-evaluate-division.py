class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Construct the graph 
        graph = defaultdict(dict) 
        for (x, y), val in zip(equations, values): 
            graph[x][y] = val 
            graph[y][x] = 1.0 / val 

        # DFS function to find the product of weights from source to target 
        def dfs(src, tgt, visited): 
            if src not in graph or tgt not in graph: 
                return -1.0 
            if src == tgt: 
                return 1.0 
            visited.add(src) 
            for neighbor, val in graph[src].items(): 
                if neighbor not in visited: 
                    res = dfs(neighbor, tgt, visited) 
                    if res != -1: 
                        return val * res 
            return -1.0 

        # Calculate results for each query 
        res = [] 
        for x, y in queries: 
            visited = set() 
            val = dfs(x, y, visited) 
            res.append(val) 

        return res 
                                                                                                                                                                                                                                                                                                                                       
