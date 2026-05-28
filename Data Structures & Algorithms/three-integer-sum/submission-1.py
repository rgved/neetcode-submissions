class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array to handle duplicates easily
        
        for i in range(len(nums) - 2):
            # Step 2: Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Use two pointers for the remaining part of the array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Sum is too small, move left pointer right
                elif total > 0:
                    right -= 1  # Sum is too large, move right pointer left
                else:
                    # Found a triplet!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return res
