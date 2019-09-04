'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
'''
核心：
1. 滑动窗口

问题：
slide_window.find(cur)效率比较低，可以换成HashTable，因为这个字符串slide_window是不含重复字符的
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        slide_window = s[0]
        max_length = 1
        for i in range(1, len(s)):
            cur = s[i]
            index = slide_window.find(cur)
            if index == -1:
                slide_window = slide_window + cur
                max_length = max(max_length, len(slide_window))
            else:
                slide_window = slide_window[index + 1:] + cur
        
        return max_length

Solution().lengthOfLongestSubstring("pwwkew")