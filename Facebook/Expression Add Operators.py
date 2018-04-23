"""
Given a string that contains only digits 0-9 and a target value, return all
possibilities to add binary operators (not unary) +, -, or * between the digits
so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """
    def addOperators(self, num, target):
        self.target = target
        self.res = []
        for i in range(1, len(num)+1):
            if i > 1 and num[0] == '0':
                continue
            self.dfs(num[i:], int(num[:i]), num[:i], int(num[:i]), '#')
        return self.res

    def dfs(self, s, sum, tmp, pre_num, pre_op):
        if not s:
            if sum == self.target:
                self.res.append(tmp[:])
            return

        for i in range(1, len(s) +1):
            if i > 1 and s[0] == '0':
                continue
            val = int(s[:i])
            self.dfs(s[i:], sum+val, tmp+'+'+s[:i], val, '+')
            self.dfs(s[i:], sum-val, tmp+'-'+s[:i], val, '-')
            if pre_op == '+':
                self.dfs(s[i:], sum - pre_num + pre_num*val, tmp+'*'+s[:i], pre_num*val, pre_op)
            elif pre_op == '-':
                self.dfs(s[i:], sum + pre_num - pre_num*val, tmp+'*'+s[:i], pre_num*val, pre_op)
            else:
                self.dfs(s[i:], sum*val, tmp+'*'+s[:i], pre_num*val, pre_op)
