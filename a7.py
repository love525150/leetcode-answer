class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        stack = []
        for i in range(0, len(s)):
            stack.append(s[i])
        
        r = ""
        
        for j in range(0, len(stack)):
            n = stack.pop()
            if n == '-':
                r = '-' + r
            else:
                r += n
        
        result = int(r)
        if result > 2147483647 or result < -2147483648:
            return 0
        else:
            return result