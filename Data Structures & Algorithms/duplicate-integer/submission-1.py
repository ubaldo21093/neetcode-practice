class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ubiset = set()
        for i in range(0, len(nums)):
            if nums[i] not in ubiset:
                ubiset.add(nums[i])
            else: 
                return True
        return False

        