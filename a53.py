class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == 0:
                max_sum = nums[i]
                last_sum = nums[i]
                continue
            
            if last_sum < 0:
                last_sum = nums[i]
            else:
                last_sum = last_sum + nums[i]

            if last_sum > max_sum:
                max_sum = last_sum
        
        return max_sum
