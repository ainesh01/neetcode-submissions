class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        checked = set()
        maxLength = 0
        for num in numSet:
            if num in checked:
                continue
            else:
                length = 1
                checked.add(num)
                while num+length in numSet:
                    checked.add(num+length)
                    length +=1
                maxLength = max(maxLength, length)

        return maxLength