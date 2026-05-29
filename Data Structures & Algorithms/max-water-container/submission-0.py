class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximus=0
        prod=1
        for i in range (0,len(heights)):
            for j in range(i+1,len(heights)):
                prod=min(heights[i],heights[j]) * (j-i)
                if(maximus<prod):
                    maximus=prod
        return maximus