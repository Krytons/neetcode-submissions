class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        # Caso 1: Kadane standard → max subarray non-wrapping
        max_sum = cur_max = nums[0]
        # Caso 2: total - min subarray → max subarray wrapping
        min_sum = cur_min = nums[0]

        for num in nums[1:]:
            cur_max = num + max(cur_max, 0)
            max_sum = max(max_sum, cur_max)

            cur_min = num + min(cur_min, 0)
            min_sum = min(min_sum, cur_min)

        # Edge case: tutti negativi → min_sum == total, il "wrapping" sarebbe array vuoto
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)
        