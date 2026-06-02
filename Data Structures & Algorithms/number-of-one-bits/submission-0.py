class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        if not n or n == 0:
            return count;

        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1

        return count