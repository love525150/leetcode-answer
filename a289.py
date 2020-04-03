'''
289. 生命游戏
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

思路：暴力遍历
原地计算思路：先活后死和先死后活用另外两个标识来表示，然后直接在原数组上修改（比如先活后死用-1，先死后活用2，abs(x) == 1表示之前都是活的，x <= 0表示现在是死的）
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        r = [[0 for x in range(m)] for x in range(n)]
        for j in range(n):
            for i in range(m):
                liveCount = self.calLiveNum(board, i, j, m - 1, n - 1)
                origin = board[j][i]
                if (origin == 0 and liveCount == 3) or (origin == 1 and (liveCount == 2 or liveCount == 3)):
                    r[j][i] = 1
        
        for j in range(n):
            for i in range(m):
                board[j][i] = r[j][i]
        return r

    def calLiveNum(self, board, x, y, x_edge, y_edge):
        i1 = max(0, x - 1)
        i2 = min(x_edge, x + 1)
        j1 = max(0, y - 1)
        j2 = min(y_edge, y + 1)

        count = 0
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                if i == x and j == y:
                    continue
                if board[j][i] == 1:
                    count += 1
        
        return count

print(Solution().gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))