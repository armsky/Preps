"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same letter
cell may not be used more than once.
"""
class Solution:
    """
    @param: board: A list of lists of character
    @param: word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        if not board:
            return False
        if not word:
            return True
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, m, n, board, word, visited):
                    return True
        return False

    def dfs(self, x, y, m, n, board, word, visited):
        if not word:
            return True
        if not 0 <= x < m or not 0 <= y < n:
            return False
        if board[x][y] == word[0] and not visited[x][y]:
            visited[x][y] =1
            a = [-1, 1, 0, 0]
            b = [0, 0, -1, 1]
            for k in range(4):
                i = x+a[k]
                j = y+b[k]
                if self.dfs(i, j, m, n, board, word[1:], visited):
                    return True
            visited[x][y] =0
        return False
