class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # If one of the words is empty, return the length of the other word
        if not word1 or not word2:
            return m + n

        # Ensure that word2 is the shorter word for space optimization
        if m < n:
            word1, word2, m, n = word2, word1, n, m

        # Initialize current and previous rows
        prev = list(range(n + 1))
        curr = [0] * (n + 1)

        # Fill the dp values using current and previous rows
        for i in range(1, m + 1):
            curr[0] = i
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1

            # Swap the rows for the next iteration
            prev, curr = curr, prev

        return prev[n]
