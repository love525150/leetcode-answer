'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
'''
'''
双指针法，两个指针放在边缘的两端，要想增大面积，必须向内移动较短的那端
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        r = 0
        i = 0
        j = len(height) - 1
        while i < j:
            l = j - i
            if height[i] < height[j]:
                r = max(r, l * height[i])
                i += 1
            else:
                r = max(r, l * height[j])
                j -= 1
        
        return r