class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        low = '0' * (len(high) - len(low)) + low
        mod = 10**9 + 7

        @cache
        def count_stepping(pos, is_greater_than_low, is_less_than_high, last_digit, nonzero):
            if pos == len(high): 
                return 1
            total = 0
            start = int(low[pos]) if not is_greater_than_low else 0
            end = int(high[pos]) + 1 if not is_less_than_high else 10
            for next_digit in range(start, end):
                if not nonzero or abs(last_digit - next_digit) == 1:
                    total += count_stepping(pos + 1, 
                                            is_greater_than_low or next_digit > int(low[pos]), 
                                            is_less_than_high or next_digit < int(high[pos]), 
                                            next_digit, 
                                            nonzero or next_digit != 0)
            return total % mod

        return count_stepping(0, False, False, -1, False)
