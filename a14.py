class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        n = 0
        exit = False
        while True:
            letter_set = set()
            for s in strs:
                if len(s) == n:
                    exit = True
                    break
                
                l = s[n: n+1]
                letter_set.add(l)

            if exit:
                break

            if len(letter_set) == 1:
                result = result + letter_set.pop()
                letter_set.clear()
            else:
                break
            
            n = n + 1
        
        return result