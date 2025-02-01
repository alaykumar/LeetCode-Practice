class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = {}

        # run through the array
        for vals in nums:
            # if value is in the dict then remove it
            if vals in temp:
                temp.pop(vals)
            # if value not in dict then add it
            else:
                temp[vals] = ''
        
       
        return list(temp.keys())[0]
        
