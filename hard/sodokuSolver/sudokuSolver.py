class Solution:
   def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)

        def backtrack(idx=0):
            if idx == len(empties):
                return True 

            i, j = empties[idx]
            b = (i // 3) * 3 + j // 3

            for ch in map(str, range(1, 10)):
                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[b]:
                   
                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[b].add(ch)

                    if backtrack(idx + 1):
                        return True

                    board[i][j] = '.'
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack()

        


        
