class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0]) 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

        # Initialize the queue with the entrance and distance as 0 
        queue = deque([(entrance[0], entrance[1], 0)]) 
        # Mark the entrance as visited by converting it to a wall 
        maze[entrance[0]][entrance[1]] = '+' 

        while queue: 
            row, col, distance = queue.popleft() 

            # Check if we've reached an exit that is not the entrance 
            if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and (distance > 0): 
                return distance 

            # Check all neighbors and enqueue them if they are empty cells 
            for dr, dc in directions: 
                r, c = row + dr, col + dc 

                if 0 <= r < m and 0 <= c < n and maze[r][c] == '.': 
                    maze[r][c] = '+' 
                    queue.append((r, c, distance + 1)) 

        # If we get here, there is no path to an exit 
        return -1 
                                                                                                                                                                                                                                                                                                 
