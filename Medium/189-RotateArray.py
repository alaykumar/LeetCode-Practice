class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        """
        n = len(nums)

        # Reduce k to avoid unnecessary rotations if k > n
        k = k % n

        # Perform k rotations, one step at a time
        for _ in range(k):
            
            last = nums.pop()
            # Insert the removed element at the beginning
            nums.insert(0, last)
