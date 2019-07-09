"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。
"""
"""
解题思路：就是前后两个值不停比较就可以了，但是判断有点多
"""
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        current_length = 0
        max_length = 1
        up_flag = True
        last_num = None
        current_num = None
        has_up = False
        has_down = False
        for i in range(len(A)):
            last_num = current_num
            current_num = A[i]
            if last_num is None:
                current_length += 1
            elif up_flag and last_num < current_num:
                has_up = True
                current_length += 1
            elif (not up_flag) and last_num > current_num:
                has_down = True
                current_length += 1
            elif up_flag and last_num > current_num:
                has_down = True
                up_flag = False
                current_length += 1
            elif (not up_flag) and last_num < current_num:
                if (has_up and has_down):
                    max_length = max(max_length, current_length)
                has_up = True
                up_flag = True
                current_length = 2
            else:
                if (has_up and has_down):
                    max_length = max(max_length, current_length)
                up_flag = True
                has_up = False
                has_down = False
                current_length = 1

        if (has_up and has_down):
            max_length = max(max_length, current_length)
        

        if max_length >= 3:
            return max_length
        else:
            return 0
