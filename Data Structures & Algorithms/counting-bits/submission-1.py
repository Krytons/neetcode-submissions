class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0] * (n + 1)
        power = 1

        for index in range (1, n + 1):
            if power * 2 == index:
                power = index
            results[index] = 1 + results[index - power]

        return results 