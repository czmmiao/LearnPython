"""

arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim每个值都认为是一种面值，且认为张数是无限的。返回组成aim的最少货币数

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。


示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

 https://leetcode.cn/problems/coin-change/description/
"""

from typing import List
class Solution():
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or len(coins) == 0 or amount < 0:
            return 0
        # return self.process1(coins, 0, amount)
        return self.dp_process(coins, amount)
    def process1(self, coins: List, idx: int, rest: int) -> int:
        if rest < 0:
            return -1

        if idx == len(coins):
            return 0 if rest == 0 else -1
        else:
            ans = -1
            for zhang in range(rest // coins[idx] + 1):
                next = self.process1(coins, idx + 1, rest - zhang * coins[idx])
                if next != -1:
                    if ans == -1:
                        ans = next + zhang
                    else:
                        ans = min(ans, next + zhang)

        return ans


    def dp_process(self, arr: List, aim: int) -> int:
        if arr is None or len(arr) == 0 or aim < 0:
            return -1

        N = len(arr)
        dp = [[0] * (aim + 1) for _ in range(N + 1)]

        # 设置最后一排的值，除了dp[N][0]为0之外，其他都是-1
        for col in range(1, aim + 1):
            dp[N][col] = -1

        for idx in range(N - 1, -1, -1):
            for rest in range(aim + 1):
                dp[idx][rest] = -1  # 初始时先设置dp[i][rest]的值无效
                if dp[idx + 1][rest] != -1:
                    dp[idx][rest] = dp[idx + 1][rest]

                if rest - arr[idx] >= 0 and dp[idx][rest - arr[idx]] != -1:
                    if dp[idx][rest] == -1:
                        dp[idx][rest] = dp[idx][rest - arr[idx]] + 1
                    else:
                        dp[idx][rest] = min(dp[idx][rest], dp[idx][rest - arr[idx]] + 1)

        return dp[0][aim]

