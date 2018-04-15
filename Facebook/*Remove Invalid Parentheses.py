"""
Remove the minimum number of invalid parentheses in order to make the input
string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    # NOTE: Smart answer from Leetcode
    #思路：正扫一遍，去掉多余的），去掉任意一个，对于连续出现的“）”，总是去掉第一个。然后把字符串反过来，再来一次。O(n^2)
    def removeInvalidParentheses(self, s):

        def removeInvalidParentheses(self, s):
        res = []
        self.remove(s, res, 0, 0, ['(', ')'])
        return res

    def remove(self, s, res, last_i, last_j, pair):
        stack = 0               #Used like a stack, but only for counting
        for i in range(last_i, len(s)):
            if s[i] == pair[0]:
                stack += 1
            if s[i] == pair[1]:
                stack -= 1
            if stack >= 0:
                continue
            for j in range(last_j, i+1): #Must be i+1 to pass the corner case like Input: '('
                if s[j] == pair[1] and (j == last_j or s[j-1] != pair[1]):
                    self.remove(s[:j] + s[j+1:], res, i, j, pair)   #因为s去掉了一个字母，i和j相当于各自+1
            return
        s = ''.join(reversed(list(s)))
        if pair[0] == '(':  #Need to be reversed once
            self.remove(s, res, 0, 0, [')', '('])
        else:
            res.append(s)


        # solution BFS
        import queue
        q = queue.Queue()
        q.put(s)
        results, visited = [], set()
        visited.add(s)
        isStop = False
        while not q.empty():
            size = q.qsize()
            for k in range(size):
                s = q.get()
                if self.check_valid(s):
                    isStop = True
                    results.append(s)
                if isStop:
                    break
                for i in range(len(s)):
                    if s[i] == "(" or s[i] == ")":
                        new_s = s[:i] + s[i+1:]
                        if new_s not in visited:
                            q.put(new_s)
                            visited.add(new_s)
        if not results:
            return [""]
        return results

    def check_valid(self, s):

        counter = 0
        for c in s:
            if counter < 0:
                return False
            if c == "(":
                counter += 1
            if c == ")":
                counter -= 1
        return counter == 0
