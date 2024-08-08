class Solution:
    # Time: O(M*N*3^L)
    # space: O(L) where L is the length of the word
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or len(board) == 0:
            return False

        self.m = len(board)
        self.n = len(board[0])
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # U, D, L, R

        # Check each cell as a starting point
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:  # Start backtracking only if first character matches
                    if self.backtrack(board, word, i, j, 0):
                        return True
        return False

    def backtrack(self, board: List[List[str]], word: str, row: int, col: int, index: int) -> bool:
        # Base case: if we've matched the entire word
        if index == len(word):
            return True

        # Boundary check and cell status check
        if row < 0 or row >= self.m or col < 0 or col >= self.n or board[row][col] == '#':
            return False

        # If the current character matches the word at index
        if board[row][col] == word[index]:
            # Mark the cell as visited
            storage = board[row][col]
            board[row][col] = '#'

            # Explore all 4 directions
            for Dir in self.dirs:
                nr = row + Dir[0]
                nc = col + Dir[1]
                if self.backtrack(board, word, nr, nc, index + 1):
                    return True

            # Backtrack: restore the cell's original value
            board[row][col] = storage

        return False
