"""
给定两个数组所有的货,重量和价值,都在w和v数组里,为了方便,其中没有负数
w 为货物重量,v为货物价值
bag背包容量,不能超过这个载重
返回: 不超重的情况下,能够得到的最大价值
"""

from typing import List
class Solution():

    def maxValue1(self, w: List, v:List, bag: int) -> int:
        if not w or not v or len(w) != len(v) or len(w) == 0:
            return -1

        return self.process1(w, v, 0, bag)

    def process1(self, w: List, v:List, ind: int, bag: int) -> int:

        if (bag < 0):
            return -1

        if ind == len(w):
            return 0

        p1 = self.process1(w, v, ind+1, bag)
        p2 = 0
        next = self.process1(w, v, ind+1, bag - w[ind])
        if next != -1:
            p2 = v[ind] + next

        return max(p1, p2)
    def maxValue2(self, w: List, v:List, bag: int) -> int:
        if not w or not v or len(w) != len(v) or len(w) == 0:
            return -1

        return self.process2(w, v, bag)
    def process2(self, w: List, v:List,  bag: int) -> int:

        N = len(w)
        dp = [[0 for _ in range(bag+1)] for _ in range(N+1)]
        dp[N] = [0] * (bag+1)

        for i in range(N-1, -1, -1):
            for rest in range(bag+1):
                p1 = dp[i+1][rest]
                p2 = -1

                if rest - w[i] >= 0:
                    next = dp[i+1][rest - w[i]]
                    p2 = v[i] + next

                dp[i][rest] = max(p1, p2)
        return dp[0][bag]


weights = [ 3,2,4,7 , 3,1 ,7]
values = [ 5,6,3,19 ,12,4,2]
bag = 15
S = Solution()
print(S.maxValue1(weights, values, bag))   # 42
print(S.maxValue2(weights, values, bag))   # 42

weights = [ 3, 2, 4, 7]
values = [ 5, 6, 3, 19]
bag = 11
S = Solution()
print(S.maxValue1(weights, values, bag))   # 25
print(S.maxValue2(weights, values, bag))   # 25
