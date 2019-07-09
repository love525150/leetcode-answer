'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            sorted_str = self.sort_str(s)
            if sorted_str not in m:
                m[sorted_str] = [s]
            else:
                m[sorted_str].append(s)
        
        return list(m.values())
        
    def sort_str(self, s):
        l=list(s)
        l.sort()
        return "".join(l)