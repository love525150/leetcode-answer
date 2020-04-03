'''
堆排序

思路：
1. 先把随机数组转为最大堆
2. 不停地删除最大堆的顶点（堆顶点的删除逻辑：把堆与树的最后一个节点交换，换完之后，新的节点沉降，最后一个节点删除）
3. 节点的删除使用逻辑删除，这样可以不需要新的空间
'''
class Solution:
    def sortArray(self, nums: list) -> list:
        self.maxHeapFy(nums)
        self.heapSort(nums)
        return nums

    # 把堆变成有序的数组：算法是把堆的顶点与树的最后一个节点交换，交换完后把最后一个节点从堆中逻辑删除，新的顶点执行沉降，使得新的树保持最大堆
    # 这里有一个逻辑：如果一个堆只有顶点改变了，那么只有顶点做沉降操作，操作完的树就能保持是最大堆
    def heapSort(self, nums):
        for end in range(len(nums), 0, -1):
            self.swap(nums, 0, end - 1)
            self.sink(nums, 1, end - 1)

    # 使一个随机数组变成最大堆：算法是从最下层的节点开始，每个节点执行沉降操作（这里过滤了没有字节点的节点，起点从最后一个节点的父节点开始执行沉降操作）
    def maxHeapFy(self, nums):
        for r in range(len(nums) // 2, 0, -1):
            self.sink(nums, r, len(nums))

    # 沉降，核心方法：把顶点沉降到适合树中合适的位置
    def sink(self, nums, root, end):
        while root * 2 <= end:
            left = root * 2
            right = left + 1
            maxChild = 0
            # 比较左右子节点，找到较大者
            if right <= end and nums[right - 1] > nums[left - 1]:
                maxChild = right
            else:
                maxChild = left
            
            if nums[root - 1] < nums[maxChild - 1]:
                self.swap(nums, root - 1, maxChild - 1)
                root = maxChild
            else: # 顶点已经是最大的节点，不需要继续沉降了
                break

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def heapSort(self, nums, end):
        self.swap(nums, end - 1, 0)