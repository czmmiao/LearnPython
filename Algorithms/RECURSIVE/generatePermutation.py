"""

// 字符串的全部子序列
// 子序列本身是可以有重复的，只是这个题目要求去重
// 测试链接 : https://www.nowcoder.com/practice/92e6247998294f2c933906fdedbc6e6a

"""

from typing import List
class Solution():
    def generatePermutation(self , s: str) -> List[str]:
        if not s:
            return [""]

        str_set = set()
        self.process1(s, 0, "", str_set)

        return list(str_set)

    def process1(self, s: str, idx: int, path: str, str_set: set):
        if idx == len(s):
            return str_set.add(path)
        else:
            self.process1(s, idx + 1, path + s[idx], str_set)
            self.process1(s, idx + 1, path, str_set)