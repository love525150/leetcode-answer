'''
简化路径

以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

示例 5：

输入："/a/../../b/../c//.//"
输出："/c"

思路：用"/"切分，用栈来表示进入下层还是返回上层
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        q = []
        moves = path.split("/")
        for move in moves:
            if move == "." or move == "":
                continue
            elif move == "..":
                if len(q) > 0:
                    q.pop()
                else:
                    continue
            else:
                q.append(move)
        
        if len(q) == 0:
            return "/"
        r = ""
        for d in q:
            r = r + "/" + d
        return r

print(Solution().simplifyPath("/a//b////c/d//././/.."))