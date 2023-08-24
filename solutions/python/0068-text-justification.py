class Solution: 
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]: 
        res, line, width = [], [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
                res, line, width = res + [''.join(line)], [], 0
            line += [w]
            width += len(w)

        return res + [' '.join(line).ljust(maxWidth)]
