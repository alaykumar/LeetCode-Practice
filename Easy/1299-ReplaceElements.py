class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initialize the maximum value to -1 (as no elements exist to the right of the last element)
        mx = -1

        # Iterate through the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            
            temp = arr[i]
            # Replace the current value with the maximum value found so far
            arr[i] = mx
            # Update the maximum value if the current value is greater
            if temp > mx:
                mx = temp
        
        return arr
