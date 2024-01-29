from typing import List

def process2(self, idx: int, s: str, dp: List) -> int:
    if idx == len(s):
        return 1

    if s[idx] == '0':
        return 0

    if dp[idx] != -1:
        return dp[idx]

    if s[idx] == '*':
        ans = self.process2(idx + 1, s) * 9
    else:
        ans = self.process2(idx + 1, s)

    if idx + 1 < len(s):
        if s[idx] != "*" and s[idx + 1] != "*":
            if int(s[idx:idx + 2]) >= 10 and int(s[idx:idx + 2]) <= 26:
                ans += self.process2(idx + 2, s)
        elif s[idx] == "1" and s[idx + 1] == "*":
            ans += self.process2(idx + 2, s) * 9
        elif s[idx] == "2" and s[idx + 1] == "*":
            ans += self.process2(idx + 2, s) * 6
        elif s[idx] == "*" and s[idx + 1] > '6':
            ans += self.process2(idx + 2, s)
        elif s[idx] == "*" and s[idx + 1] <= '6':
            ans += self.process2(idx + 2, s) * 2
        elif s[idx] == "*" and s[idx + 1] == "*":
            ans += self.process2(idx + 2, s) * 15

    dp[idx] = ans
    return ans