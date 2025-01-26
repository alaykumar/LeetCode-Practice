class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pointer to track the current index
        i = 0

        while i < len(nums) - 1:
            
            # If the current element is equal to the next one, remove the next element
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
                
        return len(nums)
