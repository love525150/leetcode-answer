'''
字符串相乘

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

思路：自己实现乘法，用一个数组保存一个个乘的时候中间的值
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 1 and num1[0] == "0" or len(num2) == 1 and num2[0] == "0":
            return "0"
        
        r = [-1 for i in range(len(num1) + len(num2))]
        step = 0 # 进位记录
        for i in range(len(num1)):
            for j in range(len(num2)):
                level = i + j
                n = int(num1[len(num1) - 1 - i]) * int(num2[len(num2) - 1 - j]) # 从最低位开始乘
                oldVal = 0 if r[level] is -1 else r[level]
                newVal = n + oldVal + step # 新值 = 原位置上的值 + 当前乘积 + 进位
                if newVal < 10:
                    r[level] = newVal
                    step = 0
                else:
                    r[level] = newVal % 10
                    step = newVal // 10
            
            if step > 0: # 进位不能带到下一个循环中
                r[i + j + 1] = step
                step = 0
        
        x = ""
        for v in r[::-1]:
            if v != -1:
                x += str(v)

        return x

print(Solution().multiply("37", "25"))