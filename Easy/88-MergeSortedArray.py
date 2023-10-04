class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # counter variables for the two sorted arrays and curr insert index
        i, j, k = m-1, n-1, m+n-1
        
        # while loop to iterate over the two arrays using array 2 size
        while j >= 0:
            
            '''
            if counter of array 1 is greater than or equal to 0 and 
            array 1 value is greater than array 2 value then 
            insert array 1 value at the kth index in array 1.
            '''
            if  i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            
            # otherwise insert array 2 value at the kth index
            else:
                nums1[k] = nums2[j]
                j-=1

            k-=1
