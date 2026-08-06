class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[0] = nums[0]
            else:
                prefix[i] = nums[i]*prefix[i-1]

        for i in range(len(nums)-1,-1,-1):
            print(i)
            if i == len(nums)-1:
                postfix[len(nums)-1] = nums[len(nums)-1]
            else:
                postfix[i] = nums[i]*postfix[i+1]

        res = []
        res.append(postfix[1])
        for k in range(1,len(nums)-1, 1):
            res.append(prefix[k-1]*postfix[k+1])
        res.append(prefix[len(nums)-2])
        return res
            
