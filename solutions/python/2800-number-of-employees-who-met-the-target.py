class Solution:
    def merge(self, s1: str, s2: str) -> str:
        if s1 == s2 or s2 in s1:
            return s1
        if s1 in s2:
            return s2
        for i in range(len(s1)):
            if s2.startswith(s1[i:]):
                return s1[:i] + s2
        return s1 + s2

    def minimumString(self, a: str, b: str, c: str) -> str:
        strings = [a, b, c]
        results = []
        for p in permutations(strings):
            merged = self.merge(self.merge(p[0], p[1]), p[2])
            results.append(merged)
        return min(results, key=lambda s: (len(s), s))
