class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr= [0]*len(nums)
        suffix_arr = [0]*len(nums)
        prefix_arr[0] = nums[0]
        suffix_arr[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i-1]*nums[i]
        
        for j in range(len(nums)-2, 0, -1):
            suffix_arr[j] = suffix_arr[j+1]*nums[j]
        
        res = [0]*len(nums)
        res[0] = suffix_arr[1]
        res[len(nums)-1] = prefix_arr[len(nums)-2]

        for k in range(1, len(nums)-1):
            res[k] = prefix_arr[k-1] * suffix_arr[k+1]
        
        return res