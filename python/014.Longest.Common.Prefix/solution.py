# -*- coding: utf-8 -*-

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:  # else会在for语句正常执行完（即：没有break）的情况下执行
            return min(strs)
         
obj = Solution()
strs = ['Hello world', 'Hello jay', 'Hello morning']
print obj.longestCommonPrefix(strs)
#strs = ['world', 'word', 'wooo']
#print obj.longestCommonPrefix(strs)
