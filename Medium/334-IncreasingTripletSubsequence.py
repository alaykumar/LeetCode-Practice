class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # If the list has fewer than 3 elements, it's impossible to have a triplet.
        if len(nums) < 3:
            return False
        
        first = float('inf')   # Smallest element found so far
        second = float('inf')  # Second smallest element found so far

        # Iterate through the list to find an increasing triplet
        for num in nums:
            if num <= first:  
                first = num  
            elif num <= second:  
                second = num  
            else:  
                # If 'num' is greater than both 'first' and 'second', found a triplet
                return True  

        return False
            
            
        
