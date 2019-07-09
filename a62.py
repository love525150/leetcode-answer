'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
'''
'''
思路：动态规划
'''
'''
性能优化：1. 不用class可以减少内存消耗；2. 将dict改为二维数组使用下标访问可以提高访问速度
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def upper(self):
        return Point(self.x, self.y - 1)
    
    def lefter(self):
        return Point(self.x - 1, self.y)
    
    def __hash__(self):
        result = 1
        result = result * 31 + self.x
        result = result * 31 + self.y
        return hash(result)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Solution(object):
    def __init__(self):
        self.cache = {}

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                p = Point(i, j)
                if i == 1 and j == 1:
                    self.cache[p] = 1
                    continue
                
                up = p.upper()
                lp = p.lefter()
                unum = self.cache.get(up, 0)
                lnum = self.cache.get(lp, 0)
                self.cache[p] = unum + lnum

        return self.cache.get(Point(m, n))

if __name__ == "__main__":
    s = Solution()
    n = s.uniquePaths(23, 12)
    print(n)
    