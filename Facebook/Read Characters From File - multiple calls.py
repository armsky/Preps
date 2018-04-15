"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.

 Notice
The read function may be called multiple times.
"""
"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""

class Solution:

    def __init__(self):
        self.i4 = 0             # point to current ele in buf4
        self.b4 = 0             # length of buf4
        self.buf4 = [None] *4

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        res = 0
        while res < n:
            if self.i4 == self.b4:
                self.b4 = Reader.read4(self.buf4)
                self.i4 = 0
                if self.b4 == 0:
                    break
            buf[res] = self.buf4[self.i4]   # need to update buf
            self.i4 += 1
            res += 1
        return res
