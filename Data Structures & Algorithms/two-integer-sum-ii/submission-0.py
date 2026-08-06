class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = 1
        while numbers[slow] + numbers[fast] != target:
            if fast == len(numbers) - 1 or numbers[slow] + numbers[fast] >target:
                slow += 1
                fast = slow+1
            else:
                fast+=1
        return [slow+1,fast+1]