'''
914. 卡牌分组
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

思路：统计各张牌的数量，满足各个数量有大于1的公约数
'''
class Solution:
    def hasGroupsSizeX(self, deck:list) -> bool:
        count = {}
        for x in deck:
            if count.get(x) is None:
                count[x] = 1
            else:
                count[x] = count[x] + 1
        
        l = list(count.values())

        if len(l) == 1:
            if l[0] > 1:
                return True
            else:
                return False
        l.sort()
        base = self.commonBase(l[0], l[1])
        if base is None:
            return False

        for i in range(len(l)):
            if l[i] % base != 0:
                return False
        
        return True

    def commonBase(self, x, y):
        start = min(x, y)
        end = max(x, y)
        for i in range(2, start + 1):
            if  x % i == 0 and y % i == 0:
                return i
        
        return None

print(Solution().hasGroupsSizeX([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]))