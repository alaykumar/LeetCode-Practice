class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # variables t keep track of top 3 maximum values
        m1, m2, m3 = float(-inf), float(-inf), float(-inf)

        # creating a set of unique digits from the nums array
        unique = set(nums)
        
        # for loop to iterate through the set ti find the top 3 max values 
        for val in unique:
            
            # if condition for max 1
            if val > m1:
                # if a new max is found then change max 2 and 3 as well
                m3 = m2
                m2 = m1
                m1 = val

            # condition for max 2
            elif val > m2:
                m3 = m2
                m2 = val

            # condition for max 3
            elif val > m3:
                m3 = val
        
        # condition check if array has more than 3 elements then returent the 
        # third max othewise return the maximum value
        if len(unique) >= 3:
            return m3
        else:
            return m1
