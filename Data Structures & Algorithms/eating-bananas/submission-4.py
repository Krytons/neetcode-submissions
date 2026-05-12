class Solution:
    maxBananas = 0

    def areEnoughHours(self, piles, k, h):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/k)
        return hours <= h;

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for pile in piles:
            if pile > self.maxBananas:
                self.maxBananas = pile

        low = 1
        mid = 0
        high = self.maxBananas

        while low < high:
            mid = ((low + high) // 2)
            isEnough = self.areEnoughHours(piles,mid, h)
            if (isEnough):
                high = mid
            else:
                low = mid + 1

        return low
            