import re  # Importing Regular Expression module

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Identifying Alice's and Bob's plays using RegEx patterns and summing them up
        alice_plays = sum(len(match.group()) - 2 for match in re.finditer(r'A{3,}', colors))
        bob_plays = sum(len(match.group()) - 2 for match in re.finditer(r'B{3,}', colors))
        
        return alice_plays > bob_plays  # Determine the winner based on the number of plays
