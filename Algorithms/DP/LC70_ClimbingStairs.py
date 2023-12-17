"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶


提示：

1 <= n <= 45

https://leetcode.cn/problems/climb-stairs/description/
"""


def climb_stairs1(n: int):
    if n == 1 or n == 2:
        return n
    return climb_stairs1(n-1) + climb_stairs1(n -2)


class Solution2:
    def climbStairs(self, n: int) -> int:
        passed = [0] * (n + 1)
        return self.climb_stairs2(n, passed)

    def climb_stairs2(self, n: int, passed: list):
        if n == 1 or n == 2:
            return n

        if passed[n] != 0:
            return passed[n]
        else:
            ans = self.climb_stairs2(n - 1, passed) + self.climb_stairs2(n - 2, passed)
            passed[n] = ans
            return passed[n]


class Solution3:
    def climbStairs(self, n: int) -> int:
        passed = [0] * (n + 1)
        return self.climb_stairs2(n, passed)

    def climb_stairs2(self, n: int, passed: list):
        if n == 1 or n == 2:
            return n

        if passed[n] != 0:
            return passed[n]
        else:
            ans = self.climb_stairs2(n - 1, passed) + self.climb_stairs2(n - 2, passed)
            passed[n] = ans
            return passed[n]




