class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a hash table (dictionary) to store indicies of array numbers
        ans = {}

        
        l = len(nums)

        # for loop to iterate through the array
        for i in range(l):

            # calculate the difference between the target and array value
            diff = target - nums[i]

            # if the difference is in the hash map then return the hash map value and the current 
            # numbers indicies otherwise add the indicices and the value in the hashmap
            if diff in ans:
                return [ans[diff], i]
            ans[nums[i]] = i

        # return ampty array if no pair is found
        return []
