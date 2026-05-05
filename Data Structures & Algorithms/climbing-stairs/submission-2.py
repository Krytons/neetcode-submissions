class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for value in range(2,n+1):
            if value%2 == 0:
                a = a + b
            else:
                b = a + b

        return a if n%2 == 0 else b



        