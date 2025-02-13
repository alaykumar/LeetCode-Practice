class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        l = 0
        r = len(nums) - 1

        # while loop to iterate through the array as it is 
        # continously divid into 2 halfs
        while l <= r:

            # calculating for the middle index of the array 
            # to determine whether to move to the left or the 
            # right of the array
            mid = (l + r) // 2

            # if the mid index value is less than the target then
            # left index is now middle plus 1
            if nums[mid] < target:
                l = mid+1
            
            # if the mid index value is greater than the target then
            # right index is now middle minus 1
            elif nums[mid] > target:
                r = mid-1
            
            
            else:
                return mid
    
        return l
