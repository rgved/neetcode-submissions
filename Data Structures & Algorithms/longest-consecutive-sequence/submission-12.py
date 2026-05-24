class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count=0
        curr=1
        sorted_nums=sorted(set(nums))
        if len(sorted_nums)==1:
            return 1
        else:
            for i in range(1,len(sorted_nums)):
                if sorted_nums[i-1]+1==sorted_nums[i]:
                    curr+=1
                    
                elif sorted_nums[i-1]+1!=sorted_nums[i]:
                    curr=0
                    curr+=1
                    
                if curr>max_count:
                    max_count=curr
        return max_count
                