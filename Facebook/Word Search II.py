"""
Given a matrix of lower alphabets and a dictionary. Find all words in the
dictionary that can be found in the matrix. A word can start from any position
in the matrix and go left/right/up/down to the adjacent position.



Have you met this question in a real interview?
Example
Given matrix:

doaf
agai
dcan
and dictionary:

{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}

"""
class Node:

    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isWord = True

    def hasWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isWord


class Solution:
    """
    @param: board: A list of lists of character
    @param: words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if not board or not words:
            return []
        root = self.getDictRoot(words)
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        res = set()
        for i in range(m):
            for j in range(n):
                self.search(i,j,m,n,board,root,'',res,visited)
        return list(res)

    def search(self, i, j, m, n, board, node, chars, res, visited):
        if node.isWord:
            res.add(chars) # Should not return here
        if not 0<=i<m or not 0<=j<n or visited[i][j]:
            return
        char = board[i][j]
        if char not in node.children:
            return
        visited[i][j] = 1 # Set here and reset later
        new_node = node.children[char]
        chars += char
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        for k in range(4):
            a = i + x[k]
            b = j + y[k]
            self.search(a,b,m,n,board,new_node,chars,res,visited)
        visited[i][j] = 0
        chars == chars[:-1]
        return

    def getDictRoot(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.root
