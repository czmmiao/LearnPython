"""
342. 4的幂
简单
相关标签
相关企业
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x



示例 1：

输入：n = 16
输出：true
示例 2：

输入：n = 5
输出：false
示例 3：

输入：n = 1
输出：true

https://leetcode.cn/problems/power-of-four/description/

"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and bin(n).count('1') == 1 and bin(n).count('0') & 1 == 1
        if n <= 0 or n != (n & -n):
            return False

        highest_one = n & -n
        cnt = 1

        while highest_one != 0:
            if highest_one & 1 == 1:
                break
            highest_one = (highest_one & 0xFFFFFFFF) >> 1
            cnt += 1
        return n > 0 and (cnt % 2 == 1)
