"""

给定一个整型数组arr，代表数值不同的纸牌排成一条线。玩家A和玩家B依次拿走每张纸
牌，规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家A
和玩家B都绝顶聪明。请返回最后获胜者的分数。
【举例】
arr=[1,2,100,4]。
开始时，玩家A只能拿走1或4。如果开始时玩家A拿走1，则排列变为[2,100,4]，接下来
玩家 B可以拿走2或4，然后继续轮到玩家A... 如果开始时玩家A拿走4，则排列变为[1,2,100]，接下来玩家B可以拿走1或100，然后继
续轮到玩家A... 玩家A作为绝顶聪明的人不会先拿4，因为拿4之后，玩家B将拿走100。所以玩家A会先拿1，
让排列变为[2,100,4]，接下来玩家B不管怎么选，100都会被玩家 A拿走。玩家A会获胜，
分数为101。所以返回101。
arr=[1,100,2]。
开始时，玩家A不管拿1还是2，玩家B作为绝顶聪明的人，都会把100拿走。玩家B会获胜，
分数为100。所以返回100。

"""


def g1(arr: list, L: int, R: int) -> int:

    if L == R:
        return 0

    result = min(f1(arr, L + 1, R), f1(arr, L, R - 1))

    return result

def f1(arr: list, L:int, R: int) -> int:
    if L == R:
        return arr[L]

    result = max(arr[L] + g1(arr, L + 1, R), arr[R] + g1(arr, L, R - 1))
    return result

def process1(arr: list):

    if not arr or len(arr) ==0:
        return 0
    L = 0
    R = len(arr) -1
    first = f1(arr, L, R)
    second = g1(arr, L, R)
    return max(first, second)

def g2(arr: list, L: int, R: int, fmap: list, gmap: list) -> int:

    if L == R:
        return 0

    if gmap[L][R] != None:
        return gmap[L][R]

    result = min(f2(arr, L + 1, R, fmap, gmap), f2(arr, L, R - 1, fmap, gmap))
    gmap[L][R] = result

    return result

def f2(arr: list, L:int, R: int, fmap: list, gmap: list) -> int:
    if L == R:
        return arr[L]

    if fmap[L][R] != None:
        return fmap[L][R]

    result = max(arr[L] + g2(arr, L + 1, R, fmap, gmap), arr[R] + g2(arr, L, R - 1, fmap, gmap))
    fmap[L][R] = result

    return result
def process2(arr: list) -> int:
    n = len(arr)
    R = n - 1
    L = 0
    fmap = [[None for _ in range(n)] for _ in range(n)]
    gmap = [[None for _ in range(n)] for _ in range(n)]

    first = f2(arr, L, R, fmap, gmap)
    second = g2(arr, L, R, fmap, gmap)
    return max(first, second)

def process3(arr: list) -> int:
    n = len(arr)
    fmap = [[-1 for _ in range(n)] for _ in range(n)]
    gmap = [[-1 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        fmap[j][j] = arr[j]
        gmap[j][j] = 0

    for j in range(1, n):
        i = 0
        while j < n:
            gmap[i][j] = min(fmap[i+1][j], fmap[i][j-1])
            fmap[i][j] = max(gmap[i+1][j] + arr[i], gmap[i][j-1] + arr[j])
            i += 1
            j += 1
    return max(gmap[0][n-1], fmap[0][n-1])


arr=[1, 100, 2]
# arr=[1,2,100,4]
result = process2(arr)
print(result)
result = process3(arr)
print(result)
