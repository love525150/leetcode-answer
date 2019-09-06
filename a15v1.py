'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
'''
'''
a + b + c = 0 --> a + b = -c，因此计算数组中所有a + b组合的值，把值作为key，（a + b）作为value存到map中；
这样再遍历nums以-c作为key就可以找到所有的组合
关键问题是不能使用重复元素，要记录a、b的下标，用以表示a、b都和c不是同一个元素
'''
from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        md = defaultdict(set)
        mi = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                v = nums[i] + nums[j]
                md[v].add((min(nums[i], nums[j]), max(nums[i], nums[j])))
                # 此处应记录i, j
        
        r = list()
        used_value = set()
        for k in range(len(nums)):
            v = nums[k]
            if v in used_value:
                continue
            key = -v
            tuples = md.get(key)
            if tuples is not None:
                for t in tuples:
                    # 此处应判断k不等于i或j
                    r.append([nums[k], t[0], t[1]])
                    used_value.add(nums[k])
                    used_value.add(t[0])
                    used_value.add(t[1])
        
        return r

print(Solution().threeSum([1,2,-2,-1]))