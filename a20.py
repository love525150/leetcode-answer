"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""
"""
解题思路：利用栈去匹对最近的一对括号
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list()
        result = True
        for index, item in enumerate(s):
            if (item == '('):
                l.append(item)
            if (item == '['):
                l.append(item)
            if (item == '{'):
                l.append(item)
            if (item == ')'):
                if (len(l) == 0):
                    result = False
                    break
                last_left = l.pop()
                if (last_left != '('):
                    result = False
                    break
            if (item == ']'):
                if (len(l) == 0):
                    result = False
                    break
                last_left = l.pop()
                if (last_left != '['):
                    result = False
                    break
            if (item == '}'):
                if (len(l) == 0):
                    result = False
                    break
                last_left = l.pop()
                if (last_left != '{'):
                    result = False
                    break
        
        return len(l) == 0 and result
