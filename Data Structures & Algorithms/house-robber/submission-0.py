class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(ind: int) -> int:
            if ind >=len(nums):
                return 0
            return max(recurse(ind+1), nums[ind]+recurse(ind+2))
        return max(recurse(0), recurse(1))