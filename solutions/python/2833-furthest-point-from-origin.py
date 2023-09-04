class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        right_moves = 0 
        left_moves = 0 
        flexible_moves = 0 
        for move in moves: 
            if move == 'R': 
                right_moves += 1 
            elif move == 'L': 
                left_moves += 1 
            elif move == '_': 
                flexible_moves += 1 
        furthest_right = right_moves - left_moves + flexible_moves 
        furthest_left = left_moves - right_moves + flexible_moves 
        return max(furthest_right, furthest_left) 
                                                                                                                                                       
