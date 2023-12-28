"""
请同学们自行搜索或者想象一个象棋的棋盘然后把整个棋盘放入第一象限，
棋盘的最左下角是(0,0)位置那么整个棋盘就是横坐标上9条线、纵坐标上10条线的区域
给你三个 参数x，y，k返回“马”从(0,0)位置出发
必须走k步最后落在(xy)上的方法数有多少种?

LC 上相似的题目
https://leetcode.cn/problems/knight-probability-in-chessboard/description/
"""

from typing import List, Union
class Solution():

    def KnightMove1(self, a:int, b:int, k: int) -> int:

        return self.process1(0, 0, a, b, k)

    def process1(self, x: int, y:int, a:int, b:int, k: int) -> int:

        if x <0 or x > 9 or y < 0 or y > 8:
            return 0

        if k == 0:
            return 1 if x == a and y == b else 0

        ways = self.process1(x + 2, y + 1, a, b, k -1)
        ways += self.process1(x - 2, y + 1, a, b, k -1)
        ways += self.process1(x + 2, y - 1, a, b, k -1)
        ways += self.process1(x - 2, y - 1, a, b, k -1)
        ways += self.process1(x + 1, y + 2, a, b, k -1)
        ways += self.process1(x - 1, y + 2, a, b, k -1)
        ways += self.process1(x + 1, y - 2, a, b, k -1)
        ways += self.process1(x - 1, y - 2, a, b, k -1)

        return ways


    # def KnightMove2(self, a:int, b:int, k: int) -> int:
    #
    #     return self.process2(0, 0, a, b, k)
    # def process2(self, col: int, row:int, a:int, b:int, k: int) -> int:
    #
    #     # dp = [[[0]*(k+1)] * 9]*10
    #     dp = [[[0] * (k + 1) for _ in range(9)] for _ in range(10)]
    #
    #     dp[0][0][0] = 1
    #
    #     for l in range(1, k+1):
    #         for y in range(9):
    #             for x in range(10):
    #                 ways = self.pick(x + 2, y + 1, k -1, dp)
    #                 ways += self.pick(x - 2, y + 1, k -1, dp)
    #                 ways += self.pick(x + 2, y - 1, k -1, dp)
    #                 ways += self.pick(x - 2, y - 1, k -1, dp)
    #                 ways += self.pick(x + 1, y + 2, k -1, dp)
    #                 ways += self.pick(x - 1, y + 2, k -1, dp)
    #                 ways += self.pick(x + 1, y - 2, k -1, dp)
    #                 ways += self.pick(x - 1, y - 2, k -1, dp)
    #                 dp[x][y][l] = ways
    #     return dp[a][b][k]
    #
    # def pick(self, x: int, y:int, k:int, dp: List) -> Union[List, int]:
    #     if x<0 or x > 10 or y < 0 or y >9 or k < 0:
    #         return 0
    #     return dp[x][y][k]
    def KnightMove2(self, x: int, y: int, step: int) -> int:
        return self.process2(x, y, step)

    def process2(self, x: int, y: int, step: int) -> int:
        dp = [[[0] * (step + 1) for _ in range(10)] for _ in range(9)]
        dp[x][y][0] = 1

        for h in range(1, step + 1):
            for r in range(9):
                for c in range(10):
                    ways = self.pick(c + 2, r + 1, h - 1, dp)
                    ways += self.pick(c - 2, r + 1, h - 1, dp)
                    ways += self.pick(c + 2, r - 1, h - 1, dp)
                    ways += self.pick(c - 2, r - 1, h - 1, dp)
                    ways += self.pick(c + 1, r + 2, h - 1, dp)
                    ways += self.pick(c - 1, r + 2, h - 1, dp)
                    ways += self.pick(c + 1, r - 2, h - 1, dp)
                    ways += self.pick(c - 1, r - 2, h - 1, dp)
                    dp[r][c][h] = ways

        return dp[0][0][step]

    def get_value(self, dp, r, c, h):
        if  r < 0 or c < 0 or r > 8 or c > 9 or h < 0:
            return 0
        return dp[r][c][h]

    def pick(self, c: int, r: int, k: int, dp: List[List[List[int]]]) -> int:
        if c < 0 or c > 9 or r < 0 or r > 8 or k <0:
            return 0
        return dp[r][c][k]



S = Solution()
x = 7
y = 7
k = 10
# print(S.KnightMove1(x, y, k))
print(S.KnightMove2(x, y, k))


def dp_ways(x, y, step):
    dp = [[[0 for _ in range(step + 1)] for _ in range(10)] for _ in range(9)]
    dp[x][y][0] = 1

    def get_value(dp, r, c, h):
        if  r < 0 or c < 0 or r > 8 or c > 9 or h < 0:
            return 0
        return dp[r][c][h]

    for h in range(1, step + 1):
        for c in range(10):
            for r in range(9):
                dp[r][c][h] += get_value(dp, r - 1, c + 2, h - 1)
                dp[r][c][h] += get_value(dp, r + 1, c + 2, h - 1)
                dp[r][c][h] += get_value(dp, r + 2, c + 1, h - 1)
                dp[r][c][h] += get_value(dp, r + 2, c - 1, h - 1)
                dp[r][c][h] += get_value(dp, r + 1, c - 2, h - 1)
                dp[r][c][h] += get_value(dp, r - 1, c - 2, h - 1)
                dp[r][c][h] += get_value(dp, r - 2, c - 1, h - 1)
                dp[r][c][h] += get_value(dp, r - 2, c + 1, h - 1)

    return dp[0][0][step]


print(dp_ways(7,7,10))