class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

    def parse(s):
        pre = None
        r = ''
        for i in range(len(s)):
            if pre is None:
                count = 1
                pre = s[i]
            elif pre == s[i]:
                pass