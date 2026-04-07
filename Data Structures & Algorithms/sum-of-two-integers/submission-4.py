class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            sum_ = a ^ b               # 不带进位的和
            carry = (a & b) << 1       # 进位（用旧 a 和旧 b）
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a ^ mask)
