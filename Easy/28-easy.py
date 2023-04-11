class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle lenght is larger than haystack, if true then return -1 
        if len(needle) > len(haystack):
            return -1
        
        # counter for haystack and needle chars respectively
        h, n = 0, 0
        
        # counter to compare the length of needle and found substring
        count = 0
        
        # variale to keep track of haystack char index
        ans = None
        
        # loop conditions to loop until h and n are less than thier respective 
        while h < len(haystack) and n < len(needle):
                          
            # if chars are equal in both strings then incrase the count of each string counter
            if haystack[h] == needle[n]:
                
                # if the index of haystack char is not stored, then repalce it with the current haystack index
                if ans == None:
                    ans = h
                
                h += 1
                n += 1
                count += 1
                
            # if the chars are not equal
            elif haystack[h] != needle[n]:
                
                # if needle counter is not 0, change the haystack counter back to the previous index of where a match was started
                if n != 0:
                    h = ans
                
                # increase haystack counter and set needle counter and length counter back to 0 and set ans to None
                h+=1
                n = 0
                count = 0
                ans = None
                
        # if match length counter and length of needle match return the haystack char index
        if count == len(needle):
            return ans
        else:
            return -1
            
                
                
        