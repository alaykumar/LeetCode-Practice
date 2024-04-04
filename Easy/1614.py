class Solution:
    def maxDepth(self, s: str) -> int:
        
        # variables to keep track of the max depth and current depth
        max_depth = 0
        curr_depth = 0

        # for loop to iterate thriugh the string
        for char in s:
            # if the currnet char is ( then increase curr_depth counter by 1
            # then update the max_depth
            if char == '(':
                curr_depth+=1
                max_depth = max(max_depth, curr_depth)
            # if char is ) then subtract from the curr_depth as a depth level has ended
            elif char == ')':
                curr_depth-=1
              
        return max_depth


        
