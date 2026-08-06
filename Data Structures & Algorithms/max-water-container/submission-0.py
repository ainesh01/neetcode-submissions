class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        first = 0
        second = 1
        while first < second and first <len(heights):
            
            if second == len(heights):
                first+=1
                second = first+1
            else:
                print(f"first: {first} second: {second}")
                area = min(heights[first], heights[second])* (second-first)
                print(f"area: {area}")
                maxArea = max(maxArea,area)
                second+=1
        return maxArea