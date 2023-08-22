class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Create empty dictionary to store seen integers and its count
        d = {}

        # for loop to iterate through the array and insert new key value pair into dict or increment existing key's values
        for i in nums:

            if i in d:
                d[i] = d[i]+1
            else:
                d[i] = 1

        # find the max key value pair using the max function
        m = max(d, key = d.get)


        # if the max value is greater or equal to 2 then return the key of that value
        if d[m] >= 2:
            return True
        
        
        return False


#### APROACH TWO ####

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      # create a hash set to keep track of ints visitied already
      visited = set()

      # for loop to iterete through the nums array
      for num in nums:

        # if the integer is in the hash set then return true
        if num in visited:
            return True

        # add the integer in the hash set if it does not exist
          visited.add(num)

      # if all ints are unique than return False
      return False
