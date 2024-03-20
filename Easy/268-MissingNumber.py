class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # get the length of the nums list
        i = len(nums)

        # calculate the sum of the first i natural numbers based on the
        # length of the nums list
        expected_sum = i * (i + 1) // 2

        # calculate the sum of the actual list
        actual_sum = sum(nums)

        # the difference between the expected and actual is the missing number
        return expected_sum - actual_sum
