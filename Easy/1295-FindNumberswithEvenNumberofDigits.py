class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        
        # for loop to iterate through the array
        for num in nums:
            
            # if the array value length mod 2 is 0 then increae the count
            if len(str(num)) % 2 == 0:
                count += 1
    
        return count
