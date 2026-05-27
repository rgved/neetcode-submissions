class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        for i in range(0,len(numbers)):
            for j in range (i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    output.append(i+1)
                    output.append(j+1)
        return output