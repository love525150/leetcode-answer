'''
最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = -1
        for s in strs:
            if min_length < 0:
                min_length = len(s)
            else:
                min_length = min(min_length, len(s))

        r = ''
        for i in range(min_length):
            c = strs[0][i]
            for s in strs:
                if c != s[i]:
                    c = None
                    break
            if c == None:
                break
            r += c

        return r

r = Solution().longestCommonPrefix(["flower","flow","flight"])
print(r)