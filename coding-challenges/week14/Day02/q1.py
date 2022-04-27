class Solution:
    def safe(self, row, col, chessboard):
        # check all attack range for queen at row, col

        # Diagonally right up
        r = row
        c = col

        while r >= 0 and c < self.n:
            if chessboard[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        # Diagonally right down
        r = row
        c = col

        while r < self.n and c < self.n:
            if chessboard[r][c] == 'Q':
                return False
            r += 1
            c += 1

        # Diagonally left up
        r = row
        c = col

        while r >= 0 and c >= 0:
            if chessboard[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Diagonally left down
        r = row
        c = col

        while r < self.n and c >= 0:
            if chessboard[r][c] == 'Q':
                return False
            r += 1
            c -= 1

        # Horizontally left
        r = row
        c = col

        while c >= 0:
            if chessboard[r][c] == 'Q':
                return False
            c -= 1

        # Horizontally right
        r = row
        c = col

        while c < self.n:
            if chessboard[r][c] == 'Q':
                return False
            c += 1

        # Vertically up
        r = row
        c = col

        while r >= 0:
            if chessboard[r][c] == 'Q':
                return False
            r -= 1

        # Vertically down
        r = row
        c = col

        while r < self.n:
            if chessboard[r][c] == 'Q':
                return False
            r += 1

        return True

    def solve(self, row, chessboard):
        if row == self.n:
            # print(chessboard)
            temp = []
            for row in chessboard:
                temp.append("".join(row))
            self.res.append(temp)
            return

        for col in range(0, self.n):
            if self.safe(row, col, chessboard):
                chessboard[row][col] = "Q"
                self.solve(row+1, chessboard)
                chessboard[row][col] = "."

    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.res = []
        chessboard = [["." for i in range(n)]for j in range(n)]
        self.solve(0, chessboard)
        return len(self.res)
