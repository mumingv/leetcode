# -*- coding: utf-8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        y = 0
        while x / 10 or x % 10:
            y = y * 10 + (x % 10)
            x = x / 10
        if abs(y) > 0x7FFFFFFF:
            return 0
        else:
            return y * sign

obj = Solution()
x = -123
print obj.reverse(x)
