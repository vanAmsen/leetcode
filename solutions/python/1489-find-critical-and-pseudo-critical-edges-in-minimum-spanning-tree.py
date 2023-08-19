# Step 1: Union-Find Data Structure
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootY] += 1
        return True

# Step 2: Main Solution
class Solution:
    # Main Method
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: [[int]]) -> [[int]]:
        
        # Step 3: Depth-First Search (DFS) Helper Function
        def dfs(node, depth, ancestor):
            levels[node] = depth
            for neighbor, edge_index in adjacency_list[node]:
                if neighbor == ancestor:
                    continue
                if levels[neighbor] == -1:
                    levels[node] = min(levels[node], dfs(neighbor, depth + 1, node))
                else:
                    levels[node] = min(levels[node], levels[neighbor])
                if levels[neighbor] >= depth + 1 and edge_index not in pseudo_critical:
                    critical.add(edge_index)
            return levels[node]

        # Step 4: Initialize Sets
        critical, pseudo_critical = set(), set()

        # Step 5: Grouping Edges By Weight
        weight_to_edges = {w: [] for w in {edge[2] for edge in edges}}
        for i, (u, v, w) in enumerate(edges):
            weight_to_edges[w].append([u, v, i])
        
        # Step 6: Using Union-Find
        union_find = UnionFind(n)
        
        # Step 7: Iterating Through Weights
        for weight in sorted(weight_to_edges):
            edge_lookup = defaultdict(set)
            
            for u, v, edge_index in weight_to_edges[weight]:
                rootU, rootV = union_find.find(u), union_find.find(v)
                
                if rootU != rootV:
                    union_pair = tuple(sorted((rootU, rootV)))
                    edge_lookup[union_pair].add(edge_index)
            
            mst_edges, adjacency_list = [], defaultdict(list)
            
            for (rootU, rootV), edge_indexes in edge_lookup.items():
                if len(edge_indexes) > 1:
                    pseudo_critical.update(edge_indexes)
                
                edge_idx = edge_indexes.pop()
                adjacency_list[rootU].append((rootV, edge_idx))
                adjacency_list[rootV].append((rootU, edge_idx))
                mst_edges.append((rootU, rootV, edge_idx))
                union_find.union(rootU, rootV)
            
            levels = [-1] * n
            
            for u, v, _ in mst_edges:
                if levels[u] == -1:
                    dfs(u, 0, -1)
            
            for _, _, edge_index in mst_edges:
                if edge_index not in critical:
                    pseudo_critical.add(edge_index)


        
        # Step 8: Return Result
        return [list(critical), list(pseudo_critical)]
