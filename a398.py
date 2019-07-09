'''
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
'''
'''
解题思路：
类的内部维护一个迭代数，当匹配的时候迭代数+1
ps.这样只是伪随机，满足出现概率一样的条件，真随机的话是每次遍历集合找出所有的索引，然后随机取一个
'''
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.indexIter = 0
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        while self.nums[self.indexIter] != target:
            self.indexIter += 1
            if self.indexIter >= len(self.nums):
                self.indexIter = 0
        
        result = self.indexIter
        self.indexIter += 1
        if self.indexIter >= len(self.nums):
                self.indexIter = 0
        return result
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)