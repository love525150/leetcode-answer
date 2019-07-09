'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26

给定一个只包含数字的非空字符串，请计算解码方法的总数。
'''
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        return self.calc(len(s) - 1, s)
    
    def calc(self, i, s):
        current = int(s[i])
        if i == 0:
            if current > 0:
                return 1
            else:
                return 0

        former = int(s[i - 1])
        if current != 0:
            if former == 1 or (former == 2 and current <= 6):
                return self.calc(i - 1, s) + 1
        else:
            if former > 2:
                return self.calc(i - 1, s) - 1
        return self.calc(i - 1, s)

s = Solution()
print(s.numDecodings('02'))
print(s.numDecodings('12'))
print(s.numDecodings('10'))
print(s.numDecodings('102'))
print(s.numDecodings('1202'))
print(s.numDecodings('1222'))
print(s.numDecodings('270270'))