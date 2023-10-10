class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        # set to keep track of visited numbers
        d = set()
        
        # for loop to check each value of the array
        for  vals in arr:
            
            # check whether the arr value * 2 is in the set or
            # if the modulo of the arr value modulo 2 is 0 and the 
            # arr value divided by 2 exists in the set then return True
            if vals*2 in d or (vals % 2 ==0 and vals//2 in d):
                return True
            
            # else add the arr value into the set
            else:
                d.add(vals)
                
        return False
                
