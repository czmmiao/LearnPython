"""
arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。每个值都认为是一种面值、且认为张数是无限的。返回组成aim的方法数
例如:arr =[1,2],aim =4
方法如下:1+1+1+1、1+1+2、2+2一共就3种方法，所以返回3

给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。

题目数据保证结果符合 32 位带符号整数。


示例 1：

输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2：

输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。
示例 3：

输入：amount = 10, coins = [10]
输出：1


https://leetcode.cn/problems/coin-change-ii/description/

"""

from typing import List

class Solution():

    def combinationSum4(self, coins: List[int], amount: int) -> int:
        if not coins or len(coins) == 0 or amount < 0:
            return 0
        return self.process1(coins, 0, amount)

    def process1(self, arr: List, idx: int, rest: int) -> int:
        if idx == len(arr):
            return 1 if rest == 0 else 0

        if rest < 0:
            return 0

        ways = 0
        zhang = 0
        while zhang*arr[idx] <= rest:
            ways += self.process1(arr, idx + 1, rest - (zhang * arr[idx]))
            zhang += 1
        return ways

    def process2(self, coins: List, amount: int) -> int:
        N = len(coins)
        dp = [[0] * (amount+1) for _ in range(N+1)]

        dp[N][0] = 1

        for idx in range(N-1, -1, -1):
            for rest in range(amount+1):
                dp[idx][rest] = dp[idx+1][rest]
                if rest - coins[idx] >= 0:
                    dp[idx][rest] += dp[idx][rest - coins[idx]]
        return dp[0][amount]
amount = 3
coins = [1, 2]

S = Solution()
process1 = S.coinChange(coins, amount)