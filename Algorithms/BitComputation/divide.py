class Solution():
    # def divide(self, a: int, b: int) -> int:
    #     ret = 0
    #     flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
    #     a, b = abs(a), abs(b)

    #     def calc(x, y):
    #         n = 1
    #         while x > y << 1:
    #             y <<= 1
    #             n <<= 1
    #         return n, y

    #     while a >= b:
    #         cnt, val = calc(a, b)
    #         ret += cnt
    #         a -= val
    #     ret = -ret if flag else ret
    #     return ret - 1 if ret >= 2 ** 31 else ret

    
    def __init__(self):
        self.x = 0xFFFFFFFF
        self.y = 0x80000000


    def add(self, a: int, b: int) -> int:

        a &= self.x
        b &= self.x

        while b != 0:
            c = (a & b ) << 1 & self.x
            a = a ^ b
            b = c

        return a if a & self.y == 0 else ~(a ^ self.x)
    def neg(self, a: int) -> int:
        return self.add(~a, 1)

    def minus(self, a: int, b: int) -> int:
        return self.add(a, self.neg(b))

    def unsigned_right_move(self, a:int, shift: int) -> int:

        return (a & self.x) >> shift

    def multiply(self, a: int, b: int) -> int:
        a &= self.x
        ans = 0
        while b != 0:
            if (b & 1) != 0:
                ans = self.add(a, ans)
            a = a << 1 & self.x
            b = self.unsigned_right_move(b, 1)

        return ans

    def divide(self, a: int, b: int) -> int:
        if b <= -2**31 and a <=-2**31:
            return 1
        
        if b <= -2**31:
            return 0
        
        return self.div(a, b)
        

    def div(self, a: int, b: int) -> int:

        x1 = self.neg(a) if a < 0 else a
        y1 = self.neg(b) if b < 0 else b

        ans = 0

        idx = 31
        while idx >=0:
            if self.unsigned_right_move(x1, idx) >= y1:
                ans |= (1 << idx)
                x1 = self.minus(x1, y1 << idx & self.x)
            idx = self.minus(idx, 1)

        ans = ans if (a <0) == (b < 0) else self.neg(ans)
        if ans > 2**31 -1:
            return 2**31 -1
        elif ans < -2**31:
            return -2**31
        else:
            return ans


S = Solution()
print(S.multiply(4000000000,500000))
print(S.minus(40000000000000000,500000))
print(S.minus(-4,-5))