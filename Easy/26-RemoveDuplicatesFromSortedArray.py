class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # for loop to iterate through the array backwoards
        for i in range(len(nums)-2, -1, -1):
            
            # if the current index number is the same as the index to its right 
            # then pop the value at the right index
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
        
        # return the array length
        return len(nums)
        
       
