"""
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

你需要原地修改栈。

示例1:

 输入：A = [2, 1, 0], B = [], C = []
 输出：C = [2, 1, 0]
示例2:

 输入：A = [1, 0], B = [], C = []
 输出：C = [1, 0]
提示:

A中盘子的数目不大于14个。

https://leetcode.cn/problems/hanota-lcci/description/

"""

from typing import List
class Solution:

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:

        n = len(A)

        return self.move(n, A, B, C)
    def move(self, n: int, A: List[int], B: List[int], C: List[int]) -> None:
        if n == 1:
            C.append(A[-1])
            A.pop()
            return C

        self.move(n-1, A, C, B)
        C.append(A[-1])
        A.pop()
        self.move(n-1, B, A, C)
    def hanota0(self,n: int) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.left_to_right(n)
    def hanota3(self, n: int) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.LtR(n)

    def LtR(self, n) -> None:
        if n == 1:
            print("Move 1 from left to right")
            return

        self.LtM(n - 1)
        print(f"Move {n} from left to right")
        self.MtR(n - 1)

    def LtM(self, n) -> None:

        if n == 1:
            print("Move 1 from left to middle")
            return

        self.LtR(n - 1)
        print(f"Move {n} from left to middle")
        self.RtM(n - 1)

    def RtM(self, n: int) -> None:

        if n == 1:
            print("Move 1 from right to middle")
            return

        self.RtL(n - 1)
        print(f"Move {n} from right to middle")
        self.LtM(n - 1)

    def MtR(self, n: int) -> None:

        if n == 1:
            print("Move 1 from middle to right")
            return

        self.MtL(n - 1)
        print(f"Move {n} from middle to right")
        self.LtR(n - 1)

    def MtL(self, n: int) -> None:

        if n == 1:
            print("Move 1 from middle to left")
            return

        self.MtR(n - 1)
        print(f"Move {n} from middle to left")
        self.RtL(n - 1)

    def RtL(self, n: int) -> None:

        if n == 1:
            print("Move 1 from right to left")
            return
        self.RtM(n - 1)
        print(f"Move {n} from right to left")
        self.MtL(n - 1)

    def hanota1(self, n: int, fr: str, to: str, other: str) -> None:

        if n == 1:
            print(f"Move 1 from {fr} to {to}")
            return

        self.hanota1(n-1, fr, other, to)
        print(f"Move {n} from {fr} to {to}")
        self.hanota1(n-1, other, to, fr)

    def left_to_right(self, n):
        if n == 1:
            print("Move 1 from left to right")
            return
        self.left_to_mid(n - 1)
        print(f"Move {n} from left to right")
        self.mid_to_right(n - 1)

    def left_to_mid(self, n):
        if n == 1:
            print("Move 1 from left to middle")
            return
        self.left_to_right(n - 1)
        print(f"Move {n} from left to middle")
        self.right_to_mid(n - 1)

    def right_to_mid(self, n):
        if n == 1:
            print("Move 1 from right to middle")
            return
        self.right_to_left(n - 1)
        print(f"Move {n} from right to middle")
        self.left_to_mid(n - 1)

    def mid_to_right(self, n):
        if n == 1:
            print("Move 1 from middle to right")
            return
        self.mid_to_left(n - 1)
        print(f"Move {n} from middle to right")
        self.left_to_right(n - 1)

    def mid_to_left(self, n):
        if n == 1:
            print("Move 1 from middle to left")
            return
        self.mid_to_right(n - 1)
        print(f"Move {n} from middle to left")
        self.right_to_left(n - 1)

    def right_to_left(self, n):
        if n == 1:
            print("Move 1 from right to left")
            return
        self.right_to_mid(n - 1)
        print(f"Move {n} from right to left")
        self.mid_to_left(n - 1)


S = Solution()
# print(S.hanota3(4))
# print(S.hanota0(4))
# print(S.hanota1(4, 'left', 'right', 'middle'))
A = [0]
B = []
C = []
print(S.hanota(A, B, C))