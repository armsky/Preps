"""
A message containing letters from A-Z is being encoded to numbers using the
following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can
be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the
total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D",
"E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n+1)]
        if not s or s.startswith('0'):
            return 0
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 1
        for i in range(2, n+1):
            first = s[i-2]
            second = s[i-1]
            # for dp[i-1]
            if second == '*':
                dp[i] += dp[i-1] * 9
            elif second > '0':
                dp[i] += dp[i-1]
            #for dp[i-2]
            if first == '*':
                if second == '*':
                    dp[i] += dp[i-2] * 15
                elif second <= '6':
                    dp[i] += dp[i-2] * 2
                else:
                    dp[i] += dp[i-2]
            elif first == '1':
                if second == '*':
                    dp[i] += dp[i-2] * 9
                else:
                    dp[i] += dp[i-2]
            elif first == '2':
                if second == '*':
                    dp[i] += dp[i-2] * 6
                elif second < '7':
                    dp[i] += dp[i-2]

            dp[i] %= 10**9 + 7

        return dp[-1]

        # Smart Solution
        one = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
        two = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1, '21': 1,
       '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2, '*5': 2, '*6': 2,
       '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = 1, one.get(s[:1], 0)

        for i in xrange(1, len(s)):
            dp = dp[1], (one.get(s[i], 0) * dp[1] + two.get(s[i-1: i+1], 0) * dp[0]) % 1000000007

        return dp[-1]
