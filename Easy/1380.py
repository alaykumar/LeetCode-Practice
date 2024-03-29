class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        # find the number of rows and columns of the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # find the mininum element in each row
        row_min = [min(row) for row in matrix]

        # find the maximum element in each column
        col_max = [max(matrix[row][col] for row in range(rows)) for col in range(cols)]

        # find the intersection of the sets of minimums and maximums
        lucky_numbers = set(row_min) & set(col_max)

        return list(lucky_numbers)

        

        
