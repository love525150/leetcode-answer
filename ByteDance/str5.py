'''
给定一个字符串，逐个翻转字符串中的每个单词。
示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

思路：栈
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        r = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if len(stack) == 0:
                    continue
                else:
                    while len(stack) > 0:
                        r += stack.pop()
                    r += " "
            else:
                stack.append(s[i])

        if len(stack) > 0:
            while len(stack) > 0:
                r += stack.pop()
        else:
            r = r[:len(r) - 1]
        return r

print(Solution().reverseWords("the sky is blue"))