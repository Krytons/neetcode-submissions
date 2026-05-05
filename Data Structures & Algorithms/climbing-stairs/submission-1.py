class Solution:

    def __init__(self) -> None:
        self.memory: dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            if n not in self.memory:
                self.memory[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.memory[n]



        