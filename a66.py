"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
"""
解题思路：就是进位哪里要处理
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = self.parseToInt(digits)
        return self.parseToList(number + 1)
        
    def parseToInt(self, digits):
        sum = 0
        le = len(digits)
        for i in range(len(digits)):
            mi = le - i - 1
            sum += (digits[i] * (10**mi))
        
        return sum

    def parseToList(self, number):
        s = str(number)
        l = []
        for i in range(len(s)):
            l.append(int(s[i]))
        return l