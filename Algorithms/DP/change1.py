"""
arr是货币数组，其中的值都是正数。再给定一个正数aim。
每个值都认为是一张货币，
即便是值相同的货币也认为每一张都是不同的，
返回组成aim的方法数
例如：arr = {1,1,1}，aim = 2
第0个和第1个能组成2，第1个和第2个能组成2，第0个和第2个能组成2
一共就3种方法，所以返回3

1、分析
货币问题III是值相同的货币没有任何不同，而此题值相同的货币认为是不同的，这是这道题的关键。
2、实现
2.1、暴力递归
先用暴力解求出，再进一步优化
从左往右的尝试模型：每张货币要不要问题
java复制代码

public static int coinWays(int[] arr, int aim) {
    return process(arr, 0, aim);
}

// arr[index....] 组成正好rest这么多的钱，有几种方法
private static int process(int[] arr, int index, int rest) {
    if (rest < 0) {
        return 0;
    }
    if (index == arr.length) { // 没钱了！
        return rest == 0 ? 1 : 0;
    }
    // 可能性一：要当前货币
    // 可能性二：不要当前货币
    return process(arr, index + 1, rest) + process(arr, index + 1, rest - arr[index]);
}

2.2、dp（填表）
根据暴力递归改动态规划，没有枚举行为，填好dp格子就是最优解
填表：index位置依赖index+1位置，所以从下往上填，从左往右填
java复制代码


public static int dp(int[] arr, int aim) {
    if (aim == 0) {
        return 1;
    }
    int N = arr.length;
    int[][] dp = new int[N + 1][aim + 1];
    dp[N][0] = 1;
    for (int index = N - 1; index >= 0; index--) {
        for (int rest = 0; rest <= aim; rest++) {
            dp[index][rest] = dp[index + 1][rest] + (rest - arr[index] >= 0 ? dp[index + 1][rest - arr[index]] : 0);
        }
    }
    return dp[0][aim];
}

作者：Mark_Zoe
链接：https://juejin.cn/post/7083140303971942414
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
from typing import List
class Solution():

    def change1(self, amount:int, coins: List[int]) -> int:
        return self.process1(coins, 0, amount)

    def change2(self, amount:int, coins: List[int]) -> int:
        return self.process2(amount, coins)


    def process1(self, arr: List, idx: int, rest: int) -> int:

        if len(arr) == 0:
            return 0
        if rest < 0:
            return 0

        if idx == len(arr):
            return 1 if rest == 0 else 0
        else:
            return self.process1(arr, idx+1, rest) + self.process1(arr, idx+1, rest-arr[idx])


    def process2(self, amount: int, coins: List[int]) -> int:
        # if amount == 0:
        #     return 1

        N = len(coins)
        dp = [[0] * (amount +1) for _ in range(N+1)]

        dp[N][0] = 1

        for idx in range(N-1, -1, -1):
            for rest in range(amount+1):
                dp[idx][rest] = dp[idx+1][rest] + (dp[idx+1][rest-coins[idx]] if rest-coins[idx] >=0 else 0)

        return dp[0][amount]




S = Solution()

import random

try_times = 100

for _ in range(try_times):
    amount = random.randint(1, 30)

    random_len = random.randint(1, 20)

    coins = [ random.randint(1, 10) for _ in range(random_len)]

    x1 = S.change1(amount, coins)
    x2 = S.change2(amount, coins)

    correct_flag = True
    if x1 != x2:
        print(f"coins:{coins}, amount:{amount}, x1:{x1}, x2{x2}")
        correct_flag = False


if correct_flag:
    print("Congratulations! The answer is perfect!")


amount = 2
coins = [1,1,1]
print(S.change1(amount, coins))
print(S.change2(amount, coins))