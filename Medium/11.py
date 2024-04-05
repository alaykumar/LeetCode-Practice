class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers, one at the start of the array and one at the end
        i = 0
        j = len(height) - 1
        
        # Initialize the variable to hold the maximum area found so far
        area = 0
        
        # Whille loop until the two pointers meet
        while i < j:
            # Calculate the area formed by the current container and update max_area if needed
            area = max(area, min(height[i], height[j]) * (j - i))
            
            # if the right pointer height is greather than the left
            # then increment the left pointer. Else decrement the right pointer.
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        # Return the maximum area found
        return area

        
