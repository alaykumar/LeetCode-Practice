class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pointer to track the current index
        i = 0

        while i < len(nums)-2:
            # If the current element is equal to the next next one, remove that element
            if nums[i] == nums[i+2]:
                nums.pop(i+2)
            else:
                i+=1

        return len(nums)

        
