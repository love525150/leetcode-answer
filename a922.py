'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。
'''
'''
解题思路：遍历一遍原数组，找到所有不合适的值，不合适分为两类：奇数不合和偶数不合，然后两类不合交换，这样是额外空间消耗比较少的方案；（第一次做的时候奇数不合跟奇数不合交换导致出错了。。）
如果不考虑额外空间，可以遍历的时候把值放进另一个数组，奇数放奇数索引，偶数放偶数索引
'''
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odds = list()
        evens = list()
        for i in range(len(A)):
            fit = self._fit(A, i)
            if fit == -1:
                continue
            if fit == 0:
                evens.append(i)
            elif fit == 1:
                odds.append(i)
        
        for i in range(len(odds)):
            self._swapValue(A, odds[i], evens[i])

        return A

    def _swapValue(self, A, i1, i2):
        temp = A[i1]
        A[i1] = A[i2]
        A[i2] = temp
    
    def _fit(self, A, index):
        if index % 2 == A[index] % 2:
            return -1
        return index % 2