from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        def findMines(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return 
            mines = 0
            if r - 1 >= 0 and board[r-1][c] == 'M': # left
                mines += 1
            if c - 1 >= 0 and board[r][c-1] == 'M': # top
                mines += 1
            if r + 1 < len(board) and board[r+1][c] == 'M': # right
                mines += 1
            if c + 1 < len(board[0]) and board[r][c+1] == 'M': # down
                mines += 1
            if r - 1 >= 0 and c - 1 >= 0 and board[r-1][c-1] == 'M': # top left
                mines += 1
            if r + 1 < len(board) and c - 1 >= 0 and board[r+1][c-1] == 'M': #bot left
                mines += 1
            if r - 1 >= 0 and c + 1 < len(board[0]) and board[r-1][c+1] == 'M': # top right
                mines += 1
            if r + 1 < len(board) and c + 1 < len(board[0]) and board[r+1][c+1] == 'M': # bot right
                mines += 1
            board[r][c] = str(mines)

        # Case 1: Mine
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board


        discovered = set()
        d = deque() 

        # Case 2: Unrevealed Empty Square
        if board[r][c] == 'E':
            findMines(r, c)
            if board[r][c] != '0':
                return board
            else:
                board[r][c] = 'B'

                discovered.add((r, c))
                d.extend([(r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1, c), (r+1,c+1)])
                while d:
                    new_r, new_c = d.popleft()
                    if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and (new_r, new_c) not in discovered:
                        findMines(new_r, new_c)
                        discovered.add((new_r, new_c))
                        if board[new_r][new_c] == '0':
                            board[new_r][new_c] = 'B'
                            d.extend([(new_r-1,new_c-1), (new_r-1,new_c), (new_r-1,new_c+1), (new_r,new_c-1), (new_r,new_c+1), (new_r+1,new_c-1), (new_r+1, new_c), (new_r+1,new_c+1)])
    
        return board