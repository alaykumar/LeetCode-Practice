class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        # create stack to append any logs with folder names
        stack = []

        # for loop to iterate through the logs
        for log in logs:
            # if the log begin swith '../' then pop from the stack of folder nams
            if log.startswith('../'):
                if stack:
                    stack.pop()

            # if the log begins with './' then remain in the same folder so 
            #continue with the log array
            elif log.startswith('./'):
                continue
            
            # append the log enttry in the stack if its not a command to go back a directory 
            # or to remian in the same directory
            else:
                stack.append(log)

        # return the remaining length of the stack
        return len(stack)
        
