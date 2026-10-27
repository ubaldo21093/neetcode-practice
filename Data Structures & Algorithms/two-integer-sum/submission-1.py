from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indxnums = {}
        for i, n in enumerate(nums):
            newtarg = target - n
            if newtarg in indxnums:
                return [indxnums[newtarg],i]
            else:
                indxnums[n] = i



