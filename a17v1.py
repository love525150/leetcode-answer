'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
mapping = dict()
mapping["2"] = ['a', 'b', 'c']
mapping["3"] = ['d', 'e', 'f']
mapping["4"] = ['g', 'h', 'i']
mapping["5"] = ['j', 'k', 'l']
mapping["6"] = ['m', 'n', 'o']
mapping["7"] = ['p', 'q', 'r', 's']
mapping["8"] = ['t', 'u', 'v']
mapping["9"] = ['w', 'x', 'y', 'z']
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        r = []
        for c in digits:
            r = self.merge(r, mapping[c])
        return r
        
    def merge(self, l1, l2):
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1
        
        r = []
        for c1 in l1:
            for c2 in l2:
                r.append(c1 + c2)
        
        return r

print(Solution().letterCombinations("23"))