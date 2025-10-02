from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in num_map:
                num_map[num].append(i)
            else:
                num_map[num] = [i]

        other_num_index = -1
        for i in range(len(nums)):
            num = nums[i]
            other_num = target - num

            if other_num not in num_map:
                continue

            other_num_index = num_map[other_num][-1]
            if other_num_index != i:
                return [i, other_num_index]
            else:
                other_num_index = -1