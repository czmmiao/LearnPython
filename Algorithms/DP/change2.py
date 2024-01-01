"""
arr是货币数组，其中的值都是正数。
再给定一个正数aim。每个值都认为是一张货币认为值相同的货币没有任何不同
返回组成aim的方法数

例如:
arr ={1,2,1,1,2,1,2}, aim =4
方法:1+1+1+1、1+1+2、2+2一共就3种方法，所以返回3

public static class Info {
    public int[] coins; // 货币数组
    public int[] zhangs; // 张数数组

    public Info(int[] c, int[] z) {
        coins = c;
        zhangs = z;
    }
}

public static int coinsWay(int[] arr, int aim) {
    if (arr == null || arr.length == 0 || aim < 0) {
        return 0;
    }
    Info info = getInfo(arr); // 统计不同货币的张数信息
    return process(info.coins, info.zhangs, 0, aim);
}

// coins 面值数组，正数且去重
// zhangs 每种面值对应的张数
private static int process(int[] coins, int[] zhangs, int index, int rest) {
    if (index == coins.length) {
        return rest == 0 ? 1 : 0;
    }
    int ways = 0;
    for (int zhang = 0; zhang * coins[index] <= rest && zhang <= zhangs[index]; zhang++) {
        ways += process(coins, zhangs, index + 1, rest - (zhang * coins[index]));
    }
    return ways;
}

private static Info getInfo(int[] arr) {
    // key：货币面值，value：货币张数
    HashMap<Integer, Integer> counts = new HashMap<>();
    for (int value : arr) {
        if (!counts.containsKey(value)) {
            counts.put(value, 1);
        } else {
            counts.put(value, counts.get(value) + 1);
        }
    }
    int N = counts.size();
    int[] coins = new int[N];
    int[] zhangs = new int[N];
    int index = 0;
    for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
        coins[index] = entry.getKey();
        zhangs[index++] = entry.getValue();
    }
    return new Info(coins, zhangs);
}

2.2、dp（填表）
根据暴力递归改动态规划
java复制代码public static int dp(int[] arr, int aim) {
    if (arr == null || arr.length == 0 || aim < 0) {
        return 0;
    }
    Info info = getInfo(arr);
    int[] coins = info.coins;
    int[] zhangs = info.zhangs;
    int N = coins.length;
    int[][] dp = new int[N + 1][aim + 1];
    dp[N][0] = 1;
    for (int index = N - 1; index >= 0; index--) {
        for (int rest = 0; rest <= aim; rest++) {
            int ways = 0;
            for (int zhang = 0; zhang * coins[index] <= rest && zhang <= zhangs[index]; zhang++) {
                ways += dp[index + 1][rest - (zhang * coins[index])];
            }
            dp[index][rest] = ways;
        }
    }
    return dp[0][aim];
}

2.3、dp（斜率优化）
发现有内层for循环，画图找邻居位置，得出依赖关系，进一步斜率优化，省掉内层for循环
java复制代码public static int dp(int[] arr, int aim) {
    if (arr == null || arr.length == 0 || aim < 0) {
        return 0;
    }
    Info info = getInfo(arr);
    int[] coins = info.coins;
    int[] zhangs = info.zhangs;
    int N = coins.length;
    int[][] dp = new int[N + 1][aim + 1];
    dp[N][0] = 1;
    for (int index = N - 1; index >= 0; index--) {
        for (int rest = 0; rest <= aim; rest++) {
            dp[index][rest] = dp[index + 1][rest];
            if (rest - coins[index] >= 0) {
                dp[index][rest] += dp[index][rest - coins[index]];
            }
            if (rest - coins[index] * (zhangs[index] + 1) >= 0) {
                dp[index][rest] -= dp[index + 1][rest - coins[index] * (zhangs[index] + 1)];
            }
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

    def coinWay1(self, amount: int, coins: List[int]) -> int:
        if amount < 0 or len(coins) == 0 or not coins:
            return 0

        values, zhangs = self.info(coins)

        return self.process1(amount, 0, values, zhangs)

    def coinWay2(self, amount: int, coins: List[int]) -> int:
        if amount < 0 or len(coins) == 0 or not coins:
            return 0

        values, zhangs = self.info(coins)

        return self.process2(amount, values, zhangs)

    def info(self, coins: List[int]) -> tuple:

        coin_dict = {}

        for coin in coins:
            coin_dict[coin] = coin_dict.get(coin, 0) + 1
        values = []
        zhangs = []

        for key, value in coin_dict.items():
            values.append(key)
            zhangs.append(value)

        return values, zhangs

    def process1(self, rest: int, idx: int, values: List, zhangs: List) -> int:
        if rest < 0:
            return 0

        N = len(values)

        if idx == N:
            return 1 if rest == 0 else 0

        ways = 0

        for zhang in range(rest// values[idx] + 1):
            if zhang <= zhangs[idx]:
                ways += self.process1(rest - zhang*values[idx], idx+1, values, zhangs)

        return ways
    def process2(self, aim: int, values: List, zhangs: List) -> int:
        if aim < 0:
            return 0

        N = len(values)

        dp = [[0] * (aim + 1) for _ in range(N + 1)]

        dp[N][0] = 1

        for idx in range(N-1, -1, -1):
            for rest in range(aim + 1):
                ways = 0
                for zhang in range(rest // values[idx] + 1):
                    if zhang <= zhangs[idx]:
                        ways += dp[idx + 1][rest - zhang * values[idx]]

                dp[idx][rest] = ways

        return dp[0][aim]

    def process3(self, aim: int, values: List, zhangs: List) -> int:
        if aim < 0:
            return 0

        N = len(values)

        dp = [[0] * (aim + 1) for _ in range(N + 1)]

        dp[N][0] = 1

        for idx in range(N-1, -1, -1):
            for rest in range(aim + 1):
                dp[idx][rest] = dp[idx+1][rest]
                if rest - values[idx] >= 0:
                    dp[idx][rest] += dp[idx][rest - values[idx]]
                if rest - values[idx]*(zhangs[idx]+1) >= 0:
                    dp[idx][rest] -= dp[idx+1][rest-values[idx]*(zhangs[idx]+1)]

        return dp[0][aim]


S = Solution()
coins = [1, 1, 2, 3, 4, 2, 5, 1]
x, y = S.info(coins)

arr =[1,2,1,1,2,1,2]
aim =4


import random

try_times = 1000

for _ in range(try_times):
    amount = random.randint(1, 100)

    random_len = random.randint(1, 100)

    coins = [ random.randint(1, 100) for _ in range(random_len)]

    # x1 = S.coinWay1(amount, coins)
    x2 = S.coinWay2(amount, coins)
    x3 = S.coinWay2(amount, coins)

    correct_flag = True
    if x3 != x2:
        print(f"coins:{coins}, amount:{amount}, x3:{x3}, x2{x2}")
        correct_flag = False
        break


if correct_flag:
    print("Congratulations! The answer is perfect!")



# print(S.info(coins))