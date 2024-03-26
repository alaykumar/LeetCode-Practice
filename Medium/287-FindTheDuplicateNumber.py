class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # for loop to itertate through the list
        for i in range(len(nums)):
            
            # Take absolute value of the current number
            num = abs(nums[i])

            # subtract one from the value to ensure the index
            # is within 1 - n
            idx = num - 1

            # if the number at the idx is negative then return
            # the number 
            if nums[idx] < 0:
                return num
            # Otherwise, make the number at the idx a negative 
            # to mark that it has been visited
            nums[idx] *= -1
