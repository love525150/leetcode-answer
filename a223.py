class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        l = self.repeatedLine(A, C, E, G)
        h = self.repeatedLine(B, D, F,H)
        repeated_s = l * h
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        return s1 + s2 - repeated_s

    def repeatedLine(self, l1s, l1e, l2s, l2e):
        if l1s > l2e or l2s > l1e:
            return 0

        len1 = l1e - l1s
        len2 = l2e - l2s
        return (len1 + len2 - abs(l1e - l2e) -abs(l1s - l2s)) // 2