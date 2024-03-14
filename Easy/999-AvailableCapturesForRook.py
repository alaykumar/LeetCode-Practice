class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        # initialzing row and column vars
        r = 0
        c = 0
        
        # for loops to locate the Rook
        for row in range(len(board)):
            for col in range(len(board)):
                
                # once the Rook position is found, store the coordinates in 
                # appropriate variables
                if board[row][col] == 'R':
                    r = row
                    c = col
        

        # initialize count var to count the number of attacks
        count = 0
        
        # ROWS CHECK
        # for loop to iterate through the rows from the Rooks position to the 0th row
        for i in range(r-1, -1, -1):
            # if any black pawns are found then incrase the count and break out of loop
            if board[i][c] == 'p':
                count+=1
                break
            # if a Biship is found then break out of the loop
            elif board[i][c] == 'B':
                break
        
        # for loop to iterate through the rows from the Rooks position to the 8th row
        for i in range(r+1, 8):
            # if any black pawns are found then incrase the count and break out of loop
            if board[i][c] == 'p':
                count+=1
                break
            # if a Biship is found then break out of the loop
            elif board[i][c] == 'B':
                break

        # COLUMN CHECK
        # for loop to iterate through the column from the Rooks position to the 0th column element
        for i in range(c-1, -1, -1):
            if board[r][i] == 'p':
                count+=1
                break
            elif board[r][i] == 'B':
                break
        
        # for loop to iterate through the column from the Rooks position to the 8th column element
        for i in range(c+1, 8):
            if board[r][i] == 'p':
                count+=1
                break
            elif board[r][i] == 'B':
                break

        # Return the count
        return count

        
