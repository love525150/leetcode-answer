'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            triangle = self.generate(1)
            triangle.append([1, 1])
            return triangle

        last_level = numRows - 1
        triangle = self.generate(last_level)
        last_row = triangle[last_level - 1]
        current_row = [1]
        for i in range(1, len(last_row)):
            current_row.append(last_row[i - 1] + last_row[i])
        current_row.append(1)
        triangle.append(current_row)
        return triangle

s = Solution()
print(s.generate(5))