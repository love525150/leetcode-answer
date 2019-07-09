class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums1)):
            key = nums1[i]
            d[key] = 1

        s = set()
        for i in range(len(nums2)):
            key = nums2[i]
            if d.get(key) == 1:
                s.add(key)

        return list(s)