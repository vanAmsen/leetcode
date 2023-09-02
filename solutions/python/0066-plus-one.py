class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        if carry:
            digits.insert(0, carry)
        return digits
