class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a hash table (dictionary) to store indicies of array numbers
        ans = {}
        
        l = len(nums)

        for i in range(l):

            # calculate the difference between the target and array value
            diff = target - nums[i]

            # if difference exists in dict, return the answer
            if diff in ans:
                return [ans[diff], i]
            ans[nums[i]] = i

        return []
