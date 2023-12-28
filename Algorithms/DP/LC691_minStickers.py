"""
给定一个字符串str，给定一个字符串类型的数组arr，出现的字符都是小写英文arr每一个字符串，代表一张贴纸，你可以把单个字符剪开使用，
目的是拼出str来返回需要至少多少张贴纸可以完成这个任务。

例子 : str="babac，arr =["ba","c","abcd"}至少需要两张贴纸”ba"和”abcd"”，
因为使用这两张贴纸，把每一个字符单独剪开，含有2个a、2个b、1个c。是可以拼出str的。所以返回2。


https://leetcode.cn/problems/stickers-to-spell-word/
"""

from typing import List, Dict
import sys
class Solution:

    def minStickers1(self, stickers: List[str], target: str) -> int:
        ans = self.process1(stickers, target)
        return -1 if ans == float('inf') else ans

    def process1(self, stickers: List[str], target: str) -> int:
        if len(target) == 0:
            return 0
        min_value = float('inf')

        for first in stickers:
            rest = self.minus_str(target, first)
            if len(rest) != len(target):
                min_value = min(min_value, self.process1(stickers, rest))

        return min_value + (0 if min_value == float('inf') else 1)

    def minus_str(self, str1: str, str2: str) -> str:

        result_freq = {}
        for cha in str1:
            result_freq[cha] = result_freq.get(cha, 0) + 1

        for cha in str2:
            result_freq[cha] = result_freq.get(cha, 0) - 1

        result_freq = {cha: freq for cha, freq in result_freq.items() if freq > 0}
        result_string = ''.join(cha*freq for cha, freq in result_freq.items())

        return result_string
    def minStickers2(self, stickers: List[str], target: str) -> int:
        ans = self.process2(stickers, target)
        return ans if ans != float('inf') else -1

    def process2(self, stickers: List[str], target: str) -> int:
        if len(target) == 0:
            return 0
        min_value = float('inf')


        for first in stickers:
            if sorted(target)[0] in first:
                rest = self.minus_str(target, first)
                if len(rest) != len(target):
                    min_value = min(min_value, self.process2(stickers, rest))

        return min_value + (0 if min_value == float('inf') else 1)

    def minStickers3(self, stickers: List[str], target: str) -> int:

        visited = {"": 0}
        ans = self.process3(stickers, target, visited)
        return ans if ans != float('inf') else -1

    def process3(self, stickers: List[str], target: str, visited: Dict) -> int:
        if target in visited:
            return visited[target]

        min_value = float('inf')

        for first in stickers:
            if sorted(target)[0] in first:
                rest = self.minus_str(target, first)
                if len(rest) != len(target):
                    min_value = min(min_value, self.process3(stickers, rest, visited))

        result = min_value + (0 if min_value == float('inf') else 1)
        visited[target] = result
        return result


    # def process1(self, stickers: List[str], target: str):
    #
    #     if len(target) == 0:
    #         return 0
    #
    #     min_value = float('inf')
    #     for first in stickers:
    #         if sorted(first)[0] == sorted(target)[0]:
    #             rest = self.minus_str(target, first)
    #             if len(rest) != len(target):
    #                 min_value = min(min_value, self.process1(stickers, rest))
    #
    #     return min_value + (0 if min_value == float('inf') else 1)
    #
    # def minus_str(self, str1: str, str2: str):
    #     result_freq = {}
    #
    #     for cha in str1:
    #         result_freq[cha] = result_freq.get(cha, 0) + 1
    #     for cha in str2:
    #         result_freq[cha] = result_freq.get(cha, 0) - 1
    #
    #     result_freq = {cha: freq for cha, freq in result_freq.items() if freq >0}
    #     # 根据词频统计结果重新生成字符串
    #     result_freq = ''.join([cha*freq for cha, freq in result_freq.items()])
    #
    #     return result_freq
    #
    # def minStickers2(self, stickers: List[str], target: str) -> int:
    #     stickers_word_freq = []
    #     for word in stickers:
    #         word_freq = {}
    #         for cha in word:
    #             word_freq[cha] = word_freq.get(cha, 0) + 1
    #         stickers_word_freq.append(word_freq)
    #
    #     target_list = sorted(target)
    #     target_dict = {}
    #     for cha in target_list:
    #         target_dict[cha] = target_dict.get(cha, 0) + 1
    #     ans = self.process2(stickers_word_freq, target_dict)
    #
    #     return ans if ans != float("inf") else -1
    #
    # def process2(self, stickers: List[Dict], target_dict: Dict):
    #     if not target_dict:
    #         return 0
    #
    #     min_value = float("inf")
    #     for sticker in stickers:
    #         if list(target_dict.keys())[0] in sticker:
    #             new_target_dict = {}
    #             for key, value in target_dict.items():
    #                     target_dict[key] = target_dict[key] - sticker.get(key, 0)
    #                     if target_dict[key] > 0:
    #                         new_target_dict[key] = target_dict[key]
    #             min_value = min(
    #                 min_value, self.process2(stickers, new_target_dict)
    #             )
    #
    #     return min_value + (0 if min_value == float("inf") else 1)
    #
    # def minStickers3(self, stickers: List, target:str) -> int:
    #
    #     sticker_list = []
    #     for sticker in stickers:
    #         word_count = [0] * 26
    #         for cha in sticker:
    #             i = ord(cha) - ord('a')
    #             word_count[i] += 1
    #
    #         sticker_list.append(word_count)
    #     ans = self.process3(sticker_list, target)
    #
    #     return ans if ans != float('inf') else -1
    #
    # def process3(self, sticker_list: List[List], target: str) -> int:
    #     if len(target) == 0:
    #         return 0
    #     target_list = [0] * 26
    #     target_list1 = [0] * 26
    #     for cha in target:
    #         i = ord(cha) - ord('a')
    #         target_list[i] += 1
    #         target_list1[i] += 1
    #
    #     min_value = float('inf')
    #     for sticker in sticker_list:
    #         if sticker[ord(target[0]) - ord('a')] > 0:
    #             rest = ''
    #             for i in range(26):
    #                 if target_list[i] > 0:
    #                     nums = target_list[i] - sticker[i]
    #                     target_list1[i] = target_list1[i] - sticker[i]
    #                     if target_list1[i] != nums:
    #                         print(f"nums: {nums}, target_list1[i]:{target_list1[i]}")
    #                     rest += chr(i + ord('a')) * nums
    #             min_value = min(min_value, self.process3(sticker_list, rest))
    #
    #     return min_value + (0 if min_value == float('inf') else 1)
    #
    # def minStickers4(self, stickers: List, target:str) -> int:
    #
    #     sticker_list = []
    #     for sticker in stickers:
    #         word_count = [0] * 26
    #         for cha in sticker:
    #             i = ord(cha) - ord('a')
    #             word_count[i] += 1
    #
    #         sticker_list.append(word_count)
    #
    #     visited = {"": 0}
    #     ans = self.process4(sticker_list, target, visited)
    #
    #     return ans if ans != float('inf') else -1
    #
    # def process4(self, sticker_list: List[List], target: str, visited: Dict) -> int:
    #
    #     if target in visited:
    #         return visited[target]
    #
    #     target_list = [0] * 26
    #     target_list1 = [0] * 26
    #     for cha in target:
    #         i = ord(cha) - ord('a')
    #         target_list[i] += 1
    #         target_list1[i] += 1
    #
    #     min_value = float('inf')
    #     for sticker in sticker_list:
    #         if sticker[ord(target[0]) - ord('a')] > 0:
    #             rest = ''
    #             for i in range(26):
    #                 if target_list[i] > 0:
    #                     nums = target_list[i] - sticker[i]
    #                     # target_list1[i] = target_list1[i] - sticker[i]
    #                     # if target_list1[i] != nums:
    #                     #     print(f"nums: {nums}, target_list1[i]:{target_list1[i]}")
    #                     rest += chr(i + ord('a')) * nums
    #             min_value = min(min_value, self.process4(sticker_list, rest, visited))
    #
    #     result = min_value + (0 if min_value == float('inf') else 1)
    #     visited[target] = result
    #
    #     return result
    #



#
# stickers = ["with","example","science"]
# target = "thehat"
#
stickers = ["these","guess","about","garden","him"]
target = "atomher"

S = Solution()
print(S.minStickers3(stickers, target))

