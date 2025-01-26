class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        # counter 
        i = 0

        l = len(arr)

        while(i < l):

            # if a 0 is encounterd, pop the last element of the array and insert a 0 at the current index then increase count of i
            if arr[i] == 0:
                arr.pop()
                arr.insert(i,0)
                i+=1

            i+=1
