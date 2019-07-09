class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_length = len(nums)
        index = 0
        while index < new_length:
            if nums[index] == val:
                self.removeElementByIndex(nums, index, new_length)
                new_length -= 1
            else:
                index += 1
        return new_length
        
    def removeElementByIndex(self, nums, index, new_length):
        if len(nums) == 1:
            nums[0] = None
        for i in range(index+1, new_length):
            nums[i - 1] = nums[i]