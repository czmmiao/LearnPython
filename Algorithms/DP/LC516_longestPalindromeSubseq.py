"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。



示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。


提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成

https://leetcode.cn/problems/longest-palindromic-subsequence/submissions/490920250/

"""

class Solution():
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        result = self.process1(s, 0, N -1)

        return result
    def process1(self, s1: str, L: int, R: int) -> int:
        if L == R:
            return 1

        if L == R-1:
            return 2 if s1[L] == s1[R] else 1

        p1 = self.process1(s1, L, R-1)
        p2 = self.process1(s1, L+1, R)
        p3 = self.process1(s1, L+1, R-1)
        p4 = self.process1(s1, L+1, R-1) + 2 if s1[L] == s1[R] else 0

        return max(p1, p2, p3, p4)

    def process2(self, s1: str) -> int:

        N = len(s1)
        dp = [[0] * N for _ in range(N)]

        dp[N-1][N-1] = 1

        for i in range(N):
            for j in range(N):
                if i == j:
                    dp[i][j] = 1
                if i == j - 1:
                    if s1[i] == s1[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1

        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                p1 = dp[i][j - 1]
                p2 = dp[i + 1][j]
                dp[i][j] = max(p1, p2)
                if s1[i] == s1[j]:
                    dp[i][j] = max(dp[i + 1][j- 1] + 2, dp[i][j])

        return dp[0][N-1]


