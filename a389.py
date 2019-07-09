'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
'''
'''
最快最省的是使用异或来计算（数学上用xor表示，python代码用^表示），核心公式是：
1. a xor a = 0
2. a xor 0 = a
3. a xor b xor a = b xor a xor a = b xor (a xor a) = b xor 0 = b
即异或偶数次等于没异或，0与a异或奇数次等于a
'''
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = 0
        for i in range(0, len(s)):
            a ^= ord(s[i])
            a ^= ord(t[i])
        
        a ^= ord(t[-1])
        return chr(a)
