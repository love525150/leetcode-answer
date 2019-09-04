'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
'''
核心：
1. 滑动窗口
2. 滑动窗口改为以i，j两个s的字符位置索引来做
3. HashTable是用来加速在滑动窗口中搜索字符位置的，hashTable的索引要更新为该字符最新的位置索引
问题：
slide_window.find(cur)效率比较低，可以换成HashTable，因为这个字符串slide_window是不含重复字符的
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = {}
        max_length = 0
        i = j = 0
        while j < len(s):
            current = s[j]
            index = hashTable.get(current)
            if index is None or index < i:
                hashTable[current] = j
                max_length = max(max_length, j - i + 1)
            else:
                i = index + 1
                hashTable[current] = j

            j += 1
        
        return max_length

print(Solution().lengthOfLongestSubstring("abcabcbb"))