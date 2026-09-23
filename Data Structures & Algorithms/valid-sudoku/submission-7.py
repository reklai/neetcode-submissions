class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square = []
        for i in range(3):
            tmp = []
            for j in range(3):
                tmp.append(set())
            square.append(tmp)
        for i in range(0, 9):
            row.clear()
            col.clear()
            for j in range(0, 9):
                if row.get(board[i][j]) == None:
                    if board[i][j].isdigit() == True:
                        row[board[i][j]] = [i, j]
                else:
                    return False
                if col.get(board[j][i]) == None:
                    if board[j][i].isdigit() == True:
                        col[board[j][i]] = [j, i]
                else:
                    return False
                if board[i][j].isdigit() == True:
                    if board[i][j] in square[i//3][j//3]:
                        return False
                    else:
                        square[i//3][j//3].add(board[i][j])
        print(square)
        return True