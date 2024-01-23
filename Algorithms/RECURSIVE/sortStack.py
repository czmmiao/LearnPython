import sys

from typing import List
class Solution:

    def sortStack(self, arr: List) -> List:

        deep = self.calc_deep(arr)
        start_pos = 0
        while deep > 0:
            max_value = self.max_func(arr[start_pos:], deep)
            k = self.max_value_times(arr, deep, max_value)
            start_pos += k
            self.down_stack(arr, deep, max_value, k)
            deep -= k

        return arr

    def calc_deep(self, arr: List) -> int:
        if len(arr) == 0:
            return 0
        num = arr.pop()
        deep = self.calc_deep(arr) + 1
        arr.append(num)
        return deep

    def max_func(self, arr: List, deep: int) -> int:
        if not arr:
            return sys.maxsize

        num = arr.pop()
        restMax = self.max_func(arr, deep -1)
        max_value = min(restMax, num)
        arr.append(num)

        return max_value

    def max_value_times(self, arr: List, deep: int, max_value: int) -> int:
        if not arr:
            return 0

        num = arr.pop()
        k = self.max_value_times(arr, deep-1, max_value)

        k += 1 if num == max_value else 0
        arr.append(num)

        return k
    def down_stack(self, arr: List, deep: int, max_value: int, k: int) -> None:
        if deep == 0:
            for i in range(k):
                arr.append(max_value)
        else:
            num = arr.pop()
            self.down_stack(arr, deep - 1, max_value, k)
            if num != max_value:
                arr.append(num)


a = [40, 2, 34, 4, 40, 2, 1, 2]

S = Solution()
# print(S.calc_deep(a), len(a), a)

print(S.down_stack(a, 8, 40, 2), a)

print(S.sortStack(a))