"""
1137. 第 N 个泰波那契数
简单
相关标签
相关企业
提示
泰波那契序列 Tn 定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。



示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537


提示：

0 <= n <= 37
答案保证是一个 32 位整数，即 answer <= 2^31 - 1。

https://leetcode.cn/problems/n-th-tribonacci-number/description/
"""


class Solution:
    def tribonacci(self, n: int) -> int:

        memo = [-1] * (n + 1)
        return self.dp(n, memo)

    def dp(self, n: int, memo: list):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        if memo[n] != -1:
            return memo[n]

        ans = self.dp(n-1, memo) + self.dp(n-2, memo) + self.dp(n-3, memo)
        memo[n] = ans

        return ans