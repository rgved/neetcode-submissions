class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate=1

        left=1
        right=max(piles)

        while(left<=right):
            mid=(left+right)//2
            totalTime=0
            for i in piles:
                totalTime=totalTime+(i+mid-1)//mid

            if totalTime<=h:
                right=mid-1
            else:
                left=mid+1
        return left
                


            