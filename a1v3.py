'''
做一个从value到index的哈希表，实现快速查找，
一边构造一边查询
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = dict()
        for i in range(len(nums)):
            subtract = target - nums[i]
            index = hashTable.get(subtract)
            if index is not None and index != i:
                return [index, i]
            hashTable[nums[i]] = i
            