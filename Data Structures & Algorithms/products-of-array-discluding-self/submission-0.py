class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod=1
        output=[]

        for i in range(0,len(nums)):
            abef=[]
            for j in range(0,len(nums)):
                if i!=j:
                    abef.append(nums[j])
            for k in range(0, len(abef)):
                prod*=abef[k]
            output.append(prod)
            prod=1
                
        return output
