from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first_k = sum(nums[:k])
        summed_nums = [first_k]

        for i in range(1, len(nums) - k + 1):
            summed_nums.append(summed_nums[i - 1] + nums[i + k - 1] - nums[i - 1])

        largest_sum = summed_nums[0]
        for _sum in summed_nums:
            if _sum > largest_sum:
                largest_sum = _sum

        return largest_sum / k
