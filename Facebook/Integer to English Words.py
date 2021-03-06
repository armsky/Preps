"""
Convert a non-negative integer to its english words representation. Given input
is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
THOUSANDS = ["", "Thousand", "Million", "Billion"]

class Solution(object):

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        i = 0
        words = ''
        while num != 0:
            if num % 1000 != 0:
                words = self.helper(num % 1000) + THOUSANDS[i] + ' ' + words
            num /= 1000
            i += 1
        return words.strip()


    def helper(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return LESS_THAN_20[num] + ' ' # don't forget the tailing space
        elif num < 100:
            return TENS[num / 10] + ' ' + self.helper(num % 10)
        else:
            return LESS_THAN_20[num / 100] + ' Hundred ' + self.helper(num % 100)
        
