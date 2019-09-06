'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。 
https://leetcode-cn.com/problems/generate-parentheses/
'''
'''
回溯算法：通过递归枚举所有的结果
剪枝：在递归枚举的过程中，如果中途就能判断后续的结果肯定不满足条件，则马上结束递归，减少无用的递归分支
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self._append('(', 1, 0, result, n)
        return result
        
    def _append(self, source, leftNum, rightNum, result, n):
        if rightNum > leftNum:
            return
        if leftNum > n:
            return
        if leftNum == n and rightNum == n:
            result.append(source)
            return
        self._append(source + '(', leftNum + 1, rightNum, result, n)
        self._append(source + ')', leftNum, rightNum + 1, result, n)