"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather
all requirements up front before implementing one.
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip() + ' '
        n = len(s) - 1
        ndigits = 0
        npoints = 0
        i = 0
        if s[i] in ['+', '-']:
            i += 1
        while s[i].isdigit() or s[i]=='.':
            if s[i].isdigit():
                ndigits += 1
            elif s[i] == '.':
                npoints += 1
            i += 1
        if ndigits == 0 or npoints >= 2:
            return False
        if s[i] == 'e':
            i += 1
            if s[i] in ['+', '-']:
                i += 1
            if i == n:
                return False
            while i < n:
                if not s[i].isdigit():
                    return False
                i += 1
        return i == n
