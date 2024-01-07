"""
371. 两整数之和
中等
相关标签
相关企业
给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。



示例 1：

输入：a = 1, b = 2
输出：3
示例 2：

输入：a = 2, b = 3
输出：5


提示：

-1000 <= a, b <= 1000

https://leetcode.cn/problems/sum-of-two-integers/description/
https://leetcode.cn/problems/add-without-plus-lcci/description/
"""

class Solution():

    def getSum(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF

        a &= x
        b &= x
        while b != 0:
           c = (a & b) << 1 & x
           a = a ^b
           b = c

        return a if a & 0x80000000==0 else ~(a^x)

S = Solution()

a = 1
b = -1

print(S.getSum(a, b))




