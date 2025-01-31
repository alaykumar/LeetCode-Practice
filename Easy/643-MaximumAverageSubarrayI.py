class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Calculating initial sum of the first 'k' elements
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window from left to right
        for i in range(k, len(nums)):
            # Remove the leftmost element and add the new element
            window_sum += nums[i] - nums[i-k]
            max_sum = max(window_sum, max_sum)

        return max_sum / k
        
        








        
