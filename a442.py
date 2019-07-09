'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
'''
'''
不用额外空间的关键就是1 ≤ a[i] ≤ n，因此a[n] - 1可以作为自己在原数组的下标来使用，我的解法是将元素在原数组内通过交换换到自己所在的位置，重复的元素设为-1作为丢弃标记（但是这样效率会偏低，因为交换会导致检查的次数会变多）
'''
'''
网上找到的效率更高的算法是不进行交换，而是把该位置的值变为负值，然后取值的时候取绝对值，这样可以在不影响原来值的位置上用一个“负值”的状态表示该位置上已经“有元素”了
'''
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        result = []
        while i < len(nums):
            if nums[i] < 0:
                i += 1
                continue
            if self._fit(nums, i):
                i += 1
            elif self._fit(nums, nums[i] - 1):
                result.append(nums[i])
                nums[i] = -1 #把这个重复的值丢掉，防止之后被swap回来
                i += 1
            else:
                self._swapValue(nums, i, nums[i] - 1)
                

        return result
        
    def _swapValue(self, A, i1, i2):
        if A[i1] == A[i2]:
            return False
        temp = A[i1]
        A[i1] = A[i2]
        A[i2] = temp
        return True
    
    def _fit(self, A, index):
        return A[index] == index + 1

    def findDuplicates2(self, nums):
        r = []
        for i in range(len(nums)):
            v = abs(nums[i])
            if nums[v - 1] < 0:
                r.append(v)
            else:
                nums[v - 1] = -nums[v - 1]
        
        return r


s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))
