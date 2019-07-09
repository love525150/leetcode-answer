"""

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1): #缩短循环的次数非常有利于性能
            if haystack[i] == needle[0]:
                j = i + 1
                match = True
                for k in range(1, len(needle)):
                    if j >= len(haystack):
                        match = False
                        break

                    if haystack[j] != needle[k]:
                        match = False
                        break
                    
                    j += 1
                
                if match:
                    return i
        
        return -1
