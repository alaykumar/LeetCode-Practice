class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        # store the length of rows and columsn in m and n respectively
        m, n = len(mat), len(mat[0])

        # create a dictionary to store the key of each diagonal and the values
        diagonals = {}

        # for loops to iterate through the mat
        for i in range(m):
            for j in range(n):
                # if the key of i-j is not in the dict then store it with 
                # an empty list as its value
                if i - j not in diagonals:
                    diagonals[i-j] = []

                # if the i-j key is in the dict, then store the matrix value
                # with the appropriate key
                diagonals[i-j].append(mat[i][j])    

        # sort each list for each key in the mat
        for key in diagonals:
            diagonals[key].sort()
        
        # for loops to now retrieve each value from the dict according to 
        # its key 
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i-j].pop(0)

        return mat

        
      









            

        
