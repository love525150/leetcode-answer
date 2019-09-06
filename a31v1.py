'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
'''
看不懂题目。。
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hasBigger = False
        for i in range(1, len(nums)):
            maxI = self.findMax(nums, i)
            if nums[maxI] > nums[i - 1] and maxI != i:
                self.swapNum(nums, maxI, i)
                hasBigger = True
        if not hasBigger:
            nums.reverse()

    def findMax(self, nums, startIndex):
        maxI = startIndex
        for i in range(startIndex + 1, len(nums)):
            if nums[i] > nums[maxI]:
                maxI = i
        
        return maxI

    def swapNum(self, nums, i1, i2):
        v = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = v

a = [1,2,3]
Solution().nextPermutation(a)
print(a)