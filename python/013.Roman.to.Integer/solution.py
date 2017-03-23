# -*- coding: utf-8 -*-

# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

# 罗马数字的组数规则
# 1. 基本数字Ⅰ、X 、C 中的任何一个,自身连用构成数目,或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个；
# 2. 不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个；
# 3. V 和 X 左边的小数字只能用 I；
# 4. L 和 C 左边的小数字只能用 X；
# 5. D 和 M 左 边的小数字只能用 C；

# 思路：
# 1. 遍历取当前字符，如果后面的字符大于当前字符，则将当前字符对应的数字减去；否则就加上；
# 2. 最后一个字符，肯定是需要加上的；

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        if len(s) == 0:
            return 0

        intNum = 0
        for i in range(0, (len(s) - 1)):
            if roman[s[i]] < roman[s[i + 1]]:
                intNum -= roman[s[i]]
            else:
                intNum += roman[s[i]]
        intNum += roman[s[-1]]
        return intNum
         
obj = Solution()
s = 'DCXXI'
print obj.romanToInt(s)
