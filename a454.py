'''
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
'''
'''
解题思路：
暴力穷举的话效率是O(n4)，效率肯定是不行的，所以把A、B的计算结果缓存到一个map里面去，C、D计算的时候再从map里面找，效率变为O(n2)
'''
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum_cache = {}
        for i in range(len(A)):
            for j in range(len(B)):
                sum = A[i] + B[j]
                sum_cache[sum] = sum_cache.get(sum, 0) + 1
        
        count = 0
        for i in range(len(C)):
            for j in range(len(D)):
                sum = C[i] + D[j]
                times = sum_cache.get(-sum, 0)
                count += times
        
        return count