'''
无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

思路：滑动窗口，碰到窗口内相同的字符就截取
优化：用i，j记录字符串的前后两个索引位来表示当前的窗口，不用遍历mapping来截取
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        tempStr = ''
        max = 0
        count = 0
        for i in range(len(s)):
            c = s[i]
            if mapping.get((c)) is None:
                mapping[c] = i
                count += 1
            else:
                oldIndex = mapping.get(c)
                mapping = {k:mapping[k] for k in mapping if mapping[k] > oldIndex}
                mapping[c] = i
                count = len(mapping)

            if count > max:
                max = count
        
        return max

    
a = Solution().lengthOfLongestSubstring("bbbbb")
print(a)