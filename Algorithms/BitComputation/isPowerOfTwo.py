"""

231. 2 的幂
简单
相关标签
相关企业
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

https://leetcode.cn/problems/power-of-two/description/

"""


class Solution():

    def isPowerOfTwo(self, n: int) -> int:

        return n > 0 and n == (n & -n)