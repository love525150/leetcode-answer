'''
912. 排序数组

给你一个整数数组 nums，请你将该数组升序排列。
'''
class Solution:
    def sortArray(self, nums: list) -> list:
        r = [None for i in range(len(nums))]
        self.mergeSort(nums, 0, len(nums) - 1, r)
        return r
    
    def mergeSort(self, nums:list, start, end, result:list):
        if start == end:
            result[start] = nums[start]
            return
        else:
            mid = (start + end) // 2
            self.mergeSort(nums, start, mid, result)
            self.mergeSort(nums, mid + 1, end, result)
            
            i = start
            j = mid + 1
            current = start
            while i <= mid and j <=end:
                if nums[i] < nums[j]:
                    result[current] = nums[i]
                    i += 1
                else:
                    result[current] = nums[j]
                    j += 1
                current += 1
            
            while i <= mid:
                result[current] = nums[i]
                i += 1
                current += 1
            
            while j <= end:
                result[current] = nums[j]
                j += 1
                current += 1
            
            for x in range(start, end + 1):
                nums[x] = result[x]

print(Solution().sortArray([0]))