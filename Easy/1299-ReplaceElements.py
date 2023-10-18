class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # working backwards on the array

        # setting a variable mx to -1 
        mx = -1

        # counter to iterate through array backwards
        i = len(arr) - 1

        # while loop to iterate through the array
        while i >= 0:

            # storing the current index arr value in a temp variable
            temp = arr[i]

            # replaceing the current index value with the max (mx) value
            arr[i] = mx

            # if the temp stored value is greather than the max (mx) then
            # replace the max variable with the temp value
            if temp > mx:
                mx = temp
            
            # move the arr index to the left by one
            i-=1
        
        return arr
