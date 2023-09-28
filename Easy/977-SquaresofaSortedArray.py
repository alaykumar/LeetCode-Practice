class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # result array
        res = [0]*len(nums)
        
        # left pointer
        i = 0
        
        # right pointer
        j = len(nums) - 1
        
        # new array index tracker
        idx = len(nums)-1
        
        # while loop will run until the index of result array is greater than 0
        while idx >= 0:
              
            # if the left pointer squared value is greater or equal to the right pointer squared value  
            # then store the left pointer value in the new array using the index counter
            if nums[i]**2 >= nums[j]**2:
                res[idx] = nums[i]**2
                
                # reduce the new array index by 1 and increase the left pointer by 1
                idx-=1
                i+=1
                
            
            else:
                # else store the squared right pointer value in the result array at the result index
                res[idx] = nums[j]**2
                
                # decrease right pointer value by 1 and the result array index by 1
                j-=1
                idx-=1
        
        # return result array
        return res
            
            
            
           
            
