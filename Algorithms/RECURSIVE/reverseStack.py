"""
用递归方式将栈逆序，且不用额外空间

"""

from typing import List
class Solution():

    def reverse_stack(self, arr: List) -> List:
        if not arr:
            return None

        i = self.f(arr)
        self.reverse_stack(arr)
        arr.append(i)

        return arr

    def f(self, arr):
        result = arr.pop()

        if not arr:
            return result
        else:
            last = self.f(arr)
            arr.append(result)
            return last


a = [1,2,3]

S = Solution()
x = S.reverse_stack(a)
print(x)


def reverse(stack):
    if not stack:
        return

    i = f(stack)
    reverse(stack)
    stack.append(i)

def f(stack):
    result = stack.pop()
    if not stack:
        return result
    else:
        last = f(stack)
        stack.append(result)
        return last

# 示例调用
stack = [1, 2, 3, 4, 5]
reverse(stack)
print(stack)
