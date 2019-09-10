'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。
'''
'''
通过二分查找找到最大值，最大值处就是数组切分处
如果nums[0]大于nums[mid]，则表示最大值在mid左边，否则在mid右边
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        ri = self.searchRotationIndex(nums)
        if nums[0] <= target and nums[ri] >= target:
            start = 0
            end = ri
        else:
            start = ri + 1
            end = len(nums) - 1
        
        return self.binarySearch(start, end, nums, target)
        
         
    def searchRotationIndex(self, nums):
        start = 0
        end = len(nums) - 1
        while True:
            mid = int((end + start) / 2)
            if mid == end:
                return mid
            if nums[mid + 1] < nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    
    def binarySearch(self, start, end, nums, target):
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1

v = Solution().search([1,3], 1)
print(v)