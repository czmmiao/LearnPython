import sys

max_int = sys.maxsize
min_int = -sys.maxsize - 1

print(f"Maximum Integer Value: {max_int}")
print(f"Minimum Integer Value: {min_int}")

def print_2bit(n: int) -> str:
    res = ''
    for i in range(31, -1, -1):
        res += "0" if (n & (1 << i)) == 0 else "1"

    print(res)

    return res
#
# print_2bit(max_int)
# print_2bit(-max_int)
# print_2bit(1^2)
# print_2bit(~-1+1)
# #
#
#
# print_2bit(1<<3)
# print((bin(3)))
# print(0x4e)

def decimal_to_hexadecimal(decimal_number):
    if decimal_number < 0:
        # 将负数转换为补码表示
        decimal_number = (1 << 32) + decimal_number

    hex_string = hex(decimal_number & 0xFFFFFFFF)[2:]  # 去掉"0x"前缀，并保留低32位

    if hex_string == "":
        hex_string = "0"

    return hex_string
#
# # 示例使用
# negative_decimal_number = -255
# hex_string = decimal_to_hexadecimal(negative_decimal_number)
#
# print(f"整数 {negative_decimal_number} 转换为十六进制字符串: {hex_string}")
# print(hex(-255))
#
# # 示例使用
# negative_decimal_number = 255
# hex_string = decimal_to_hexadecimal(negative_decimal_number)
#
# print(f"整数 {negative_decimal_number} 转换为十六进制字符串: {hex_string}")
# print(hex(255))
#
# negative_decimal_number = 1
#
# hex_string = decimal_to_hexadecimal(1)
#
# print(f"整数 {negative_decimal_number} 转换为十六进制字符串: {hex_string}")
# print(hex(1))
#
# print(3 & 5)
# print_2bit(-5)
# print_2bit(-5 >> 2)
# print_2bit(-5 >> 2)
# print_2bit(5 >> 2)
#
# print(16 % 0x100000000)
# print(3 >> 3)


def unsigned_right_shit(value, shift):
    return (value % 0x10000000) >> shift

def unsigned_right_shit2(value, shift):
    return (value & 0xFFFFFFFF)>> shift

x = -8
res = unsigned_right_shit(x,1)
print_2bit(-8)
print_2bit(-8% 0x10000000)
print_2bit(res)
print_2bit(unsigned_right_shit2(x,1))
print_2bit(unsigned_right_shit2(-8,1))
print_2bit(-8>>1)
print_2bit(unsigned_right_shit2(8,1))
print_2bit(5&0x80000000)

print_2bit(~4294967295)
print_2bit(~4294967295+1)
print_2bit(4294967295)
print(0x7fffffff)
print_2bit(0x7fffffff)
print_2bit(0xFFFFFFFF)
print(11111111111111111111101111111111<0x7fffffff)
print(2**32-1)

y = 0x80000000
print(5^3)
print(5|3)
print_2bit(-8)
print_2bit(unsigned_right_shit2(-8, 3))
# print_2bit(-5)
# a = 3
# print_2bit(~a+1)
# print_2bit(-1)
#
#
# print_2bit(3 & -3)
# print_2bit(3 | -3)
# print_2bit(3 ^ -3)
# print_2bit(0 ^ 0)