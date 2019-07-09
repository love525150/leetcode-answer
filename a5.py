'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''
'''
解题思路：
动态规划：当s[i:j+1]是回文串，若s[i-1] == s[j+1]，则s[i-1:j+2]是一个更长的回文串
因此，1长度的可以找3长度的，3长度的可以找5长度的等等；而2长度的可以找4长度的，4长度的可以找6长度的等等。。。
最后就是遍历所有1长度的回文串和2长度的回文串去找最长的回文串
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        longestI = 0
        longestJ = 0
        currentIndex = 0
        while self.maxLength(currentIndex, s) > length:
            i, j = self.findPalindrome(currentIndex, currentIndex, s)
            newLength = j - i + 1
            if length < newLength:
                longestI = i
                longestJ = j
                length = newLength
            currentIndex += 1
        
        currentIndex = 0
        while self.maxLengthForDual(currentIndex, s) > length:
            if s[currentIndex] == s[currentIndex + 1]:
                i, j = self.findPalindrome(currentIndex, currentIndex + 1, s)
                newLength = j - i + 1
                if length < newLength:
                    longestI = i
                    longestJ = j
                    length = newLength
            currentIndex += 1
        
        return s[longestI:longestJ + 1]

    # 核心方法
    def findPalindrome(self, i, j, s):
        if i == 0 or j == len(s) - 1:
            return i, j
        if s[i - 1] == s[j + 1]:
            return self.findPalindrome(i - 1, j + 1, s)
        else:
            return i, j

    def maxLength(self, index, s):
        return (len(s) - 1 - index) * 2 + 1

    def maxLengthForDual(self, index, s):
        return (len(s) - 1 - index) * 2