class Solution:
    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False
        
        n, m = len(board[0]), len(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.DFS(board, word, i, j, 0, [[False] * n for _ in range(m)]):
                    return True
        return False

    def DFS(self, board, word, i, j, k, visited):
        if k == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j] or visited[i][j]:
            return False

        visited[i][j] = True
        if (self.DFS(board, word, i - 1, j, k + 1, visited) or
            self.DFS(board, word, i + 1, j, k + 1, visited) or
            self.DFS(board, word, i, j - 1, k + 1, visited) or
            self.DFS(board, word, i, j + 1, k + 1, visited)):
            return True

        visited[i][j] = False
        return False

