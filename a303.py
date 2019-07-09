'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
'''
'''
核心就是缓存从0到x的结果放在sums，把求sumRange(i,j)换成算sums[j] - sums[i - 1]，可以从一开始就是算好所有sums（比较占空间），也可以边算边缓存
'''
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = {}
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # result = sum[j] - sum[i -1] when i >= 1; result = sum[j] when i = 0
        if i == 0:
            return self.calcSum(j)
        else:
            return self.calcSum(j) - self.calcSum(i - 1)
    
    def calcSum(self, index):
        cache = self.sums.get(index)
        if self.sums.get(index) is not None:
            return cache

        r = 0
        lastIndex, lastSum = self.getLastSum(index)
        if lastSum is None:
            for i in range(0, index + 1):
                r += self.nums[i]
        else:
            r = lastSum
            for i in range(lastIndex + 1, index + 1):
                r += self.nums[i]
        self.sums[index] = r
        return r
    
    def getLastSum(self, index):
        for i in range(index - 1, 0, -1):
            sumCache = self.sums.get(i)
            if sumCache is not None:
                return i, sumCache
        
        return None, None



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)