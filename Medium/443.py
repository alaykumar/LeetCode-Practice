class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        res = 0
        
        i = 0

        # While loop to itereate through the chars
        while i < len(chars):
            
            temp = chars[i]
            
            count = 0

            # while loop to see if the following hcars are the same as the current
            while i < len(chars) and chars[i] == temp:
                count+=1
                i+=1
            
            # change the value at index of res to the current chars then increase res by 1
            chars[res] = temp
            res+=1

            # if the char count is greater than one then use a for loop to
            # append the count for each char in the chars array then increase
            # res by 1
            if count > 1:
                for x in str(count):
                    chars[res] = x
                    res+=1
        
        return res

    
