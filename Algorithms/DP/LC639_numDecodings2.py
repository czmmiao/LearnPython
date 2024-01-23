"""

解码方法 II
一条包含字母 A-Z 的消息通过以下的方式进行了 编码 ：
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
要 解码 一条已编码的消息，所有的数字都必须分组
然后按原来的编码方案反向映射回字母（可能存在多种方式）
例如，"11106" 可以映射为："AAJF"、"KJF"
注意，像 (1 11 06) 这样的分组是无效的，"06"不可以映射为'F'
除了上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符
可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）
例如，"1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19"
对 "1*" 进行解码，相当于解码该字符串可以表示的任何编码消息
给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目
由于答案数目可能非常大，返回10^9 + 7的模
测试链接 : https://leetcode.cn/problems/decode-ways-ii/

"""

from typing import List
class Solution:

    mod_num = 1000000000 + 7

    def numDecodings1(self, s: str) -> int:

        return self.process1(0, s)
    def numDecodings(self, s: str) -> int:

        N = len(s)
        dp = [-1] * (N+1)
        return self.process2(0, s, dp)

    def process1(self,idx: int, s: str) -> int:

        if len(s) == idx:
            return 1

        if s[idx] == '0':
            return 0

        if s[idx] == '*':
            ans = self.process1(idx+1, s)*9
        else:
            ans = self.process1(idx+1, s)

        if idx+1 < len(s):
            if s[idx] != "*" and s[idx+1] != "*":
                if int(s[idx:idx+2]) >=10 and int(s[idx:idx+2]) <= 26:
                    ans += self.process1(idx+2, s)
            elif s[idx] == "1" and s[idx+1] == "*":
                ans += self.process1(idx+2, s)*9
            elif s[idx] == "2" and s[idx+1] == "*":
                ans += self.process1(idx+2, s)*6
            elif s[idx] == "*" and s[idx+1] > '6':
                ans += self.process1(idx+2, s)
            elif s[idx] == "*" and s[idx+1] <= '6':
                ans += self.process1(idx+2, s)*2
            elif s[idx] == "*" and s[idx+1] == "*":
                ans += self.process1(idx+2, s)*15

        return ans

    def process2(self, idx: int, s: str, dp: List) -> int:
        if idx == len(s):
            return 1

        if s[idx] == '0':
            return 0

        if dp[idx] != -1:
            return dp[idx]

        if s[idx] == '*':
            ans = self.process2(idx + 1, s, dp) * 9
        else:
            ans = self.process2(idx + 1, s, dp)

        if idx + 1 < len(s):
            if s[idx] != "*" and s[idx + 1] != "*":
                if int(s[idx:idx + 2]) >= 10 and int(s[idx:idx + 2]) <= 26:
                    ans += self.process2(idx + 2, s, dp)
            if s[idx] == "1" and s[idx + 1] == "*":
              ans += self.process2(idx + 2, s, dp) * 9
            if s[idx] == "2" and s[idx + 1] == "*":
              ans += self.process2(idx + 2, s, dp) * 6
            if s[idx] == "*" and s[idx + 1] == "*":
                ans += self.process2(idx + 2, s, dp) * 15
            if s[idx] == "*" and s[idx + 1] != "*" and s[idx + 1] > '6':
              ans += self.process2(idx + 2, s, dp)
            if s[idx] == "*" and s[idx + 1] != "*" and  s[idx + 1] <= '6':
              ans += self.process2(idx + 2, s, dp) * 2

        ans %= self.mod_num
        dp[idx] = ans
        return ans

    def process3(self, s: str) -> int:

        N = len(s)

        dp = [0] * (N + 1)
        dp[N] = 1

        for idx in range(N - 1, -1, -1):
            if s[idx] == '0':
                continue
            if s[idx] == '*':
                dp[idx] = dp[idx + 1] * 9
            else:
                dp[idx] = dp[idx + 1]

            if idx + 1 < N:
                if s[idx] != "*" and s[idx + 1] != "*":
                    if int(s[idx:idx + 2]) >= 10 and int(s[idx:idx + 2]) <= 26:
                        dp[idx] += dp[idx + 2]
                if s[idx] == "1" and s[idx + 1] == "*":
                    dp[idx] += dp[idx + 2] * 9
                if s[idx] == "2" and s[idx + 1] == "*":
                    dp[idx] += dp[idx + 2] * 6
                if s[idx] == "*" and s[idx + 1] == "*":
                    dp[idx] += dp[idx + 2] * 15
                if s[idx] == "*" and s[idx + 1] != "*" and s[idx + 1] > '6':
                    dp[idx] += dp[idx + 2]
                if s[idx] == "*" and s[idx + 1] != "*" and s[idx + 1] <= '6':
                    dp[idx] += dp[idx + 2] * 2

            dp[idx] %= self.mod_num

        return dp[0]
    def f2(self, s: str, idx: int, dp: List[int]) -> int:
        if idx == len(s):
            return 1
        if s[idx] == '0':
            return 0
        if dp[idx] != -1:
            return dp[idx]
        ans = self.f2(s, idx + 1, dp) * (s[idx] == '*' and 9 or 1)
        if idx + 1 < len(s):
            if s[idx] != '*':
                if s[idx + 1] != '*':
                    if (ord(s[idx]) - ord('0')) * 10 + ord(s[idx + 1]) - ord('0') <= 26:
                        ans += self.f2(s, idx + 2, dp)
                else:
                    if s[idx] == '1':
                        ans += self.f2(s, idx + 2, dp) * 9
                    if s[idx] == '2':
                        ans += self.f2(s, idx + 2, dp) * 6
            else:
                if s[idx + 1] != '*':
                    if ord(s[idx + 1]) <= ord('6'):
                        ans += self.f2(s, idx + 2, dp) * 2
                    else:
                        ans += self.f2(s, idx + 2, dp)
                else:
                    ans += self.f2(s, idx + 2, dp) * 15
        ans %= self.mod_num  # assuming mod is a global variable defined outside the class
        dp[idx] = ans
        return ans