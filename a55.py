'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        currentToIndex = size - 1
        shortest FromIndex = self.canJumpTo(nums, size - 1)
        while shortesFromIndex != 0 and shortestFromIndex is not None:
            currentToIndex = shortestFromIndex
            shortest FromIndex = self.canJumpTo(nums, currentToIndex)
        
        if shorteFromIndex is not None:
            return True
        
        return False

    def canJumpTo(self, nums, toIndex):
        if toIndex == 0:
            return 0

        for startIndex in range(toIndex - 1, -1, -1):
            if toIndex - startIndex <= nums[startIndex]:
                return startIndex

if __name__ == "__main__":
    r = Solution().canJump([2,3,1,1,4])
    print(r)