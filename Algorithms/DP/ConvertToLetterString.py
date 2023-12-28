"""
规定1和A对应、2和B对应、3和C对应...26和Z对应那么一个数字字符串比如“111”就可以转化为"AAA”“KA"和”AK"
给定一个只有数字字符组成的字符串str，返回有多少种转化结果

"""
from typing import List

class Solution():
    def convert_to_letter_string1(self, str1: str) -> int:
        result = self.process1(str1, 0)
        return result

    def process1(self, str1: str, ind: int) -> int:
        if ind == len(str1):
            return 1

        if str1[ind] == '0':
            return 0

        result = self.process1(str1, ind+1)
        if int(str1[ind: ind+2]) <= 26 and ind+1 < len(str1):
            result += self.process1(str1, ind+2)

        return result
    def convert_to_letter_string2(self, str1: str) -> int:

        result = self.process2(str1)
        return result

    def process2(self, str1: str) -> int:
        N = len(str1)
        dp = [0] * (N + 1)
        dp[N] = 1
        for i in range(N-1, -1, -1):
            if str1[i] == '0':
                dp[i] = 0
            if str1[i] != '0':
                ways = dp[i+1]
                if int(str1[i: i+2]) <= 26 and i+1 < len(str1):
                    ways += dp[i+2]
                dp[i] = ways
        return dp[0]


S = Solution()
# print(S.convert_to_letter_string1('7210231231232031203123'))
# print(S.convert_to_letter_string2('7210231231232031203123'))
# print(S.convert_to_letter_string1('7230231231232031203123'))
# print(S.convert_to_letter_string2('7230231231232031203123'))
print(S.convert_to_letter_string1('929'))
