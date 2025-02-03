class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        # for loop to iterate through the logs
        for log in logs:
            # if the log begin swith '../' then pop from the stack of folder names
            if log.startswith('../'):
                if stack:
                    stack.pop()

            # if the log begins with './' then remain in the same folder so 
            #continue with the log array
            elif log.startswith('./'):
                continue
            
            else:
                stack.append(log)

        
        return len(stack)
        
