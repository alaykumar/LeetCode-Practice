class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # Edge case for only single element arrays
        if len(nums) == 1:
            return nums
        
        # pointer one to keep track of comparison value index
        i = 0

        # for loop to iterate through the array (j as pointer two)
        for j in range(len(nums)):

            # if the current value has modulo equal to 2 then swap the array
            # valeus at index i and j and increase count of comparison value
            # pointer (i)
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            
        return nums
