class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # initialize variables for counter and max count
        count = 0
        mx = 0

        # length of the nums array
        l = len(nums)

       # for loop to iterate through the array 
        for num in range(l):

           # if the arr value is 1 then increase the count
            if nums[num] == 1:
                count+=1
            # else reset count back to 0
            else:
                count = 0
            # store the maximum of eother the current max or the old max into the mx varibale
            mx = max(mx, count)

       # return the max
        return mx
        
