"""
1、题目
给定一个正数 n nn，求 n nn 的裂开方法数。

规定：后面的数不能比前面的数小。

比如 4 的裂开方法有：① 1 + 1 + 1 + 1；② 1 + 1 + 2；③ 1 + 3；④ 2 + 2；⑤ 4。一共 5 种，所以返回 5。

2、思路
2.1 暴力递归版本
public class SplitNumber {
    // n 为正数
    public static int ways(int n) {
        if (n < 0) return 0;

        if (n == 1) return 1;

        return process(1, n);
    }

    //上一个拆出来的数是pre
    //还剩rest需要去拆
    //返回拆解的方法数
    public static int process(int pre, int rest) {
        if (rest == 0) { //认为到达了拆分的终结点，之前的规则都没有违反，所以找到了一种有效的拆分方法 比如7 直接拆分为7，这也是一种方法
            return 1;
        }

        if (pre > rest) {
        	return 0;
        }

        if (pre == rest) { //当pre=rest时，rest只能用rest这个值不能再拆了，否则就会小于pre了，所以只有一种方法，比如6 = 3+3,后面一个3不能再拆了
            return 1;
        }

        //剩下的情况 pre < rest
        int ways = 0;
        for (int first = pre; first <= rest; first++) { //rest拆分尝试
            ways += process(first, rest - first);
        }
        return ways;
    }
}

2.2 动态规划版本
public class SplitNumber {
    // n 为正数
    public static int ways(int n) {
        if (n < 0) return 0;

        if (n == 1) return 1;

        int[][] dp = new int[n + 1][n + 1];
    	//pre没有等于0的时候，所以dp表第0行是没有用
        for (int pre = 1; pre <= n; pre++) {
            dp[pre][0] = 1; //第0列
            dp[pre][pre] = 1; //对角线
        }

        //普遍位置
        for (int pre = n - 1; pre >= 1; pre--) {
            for (int rest = pre + 1; rest <= n; rest++) {
                int ways = 0;
                for (int first = pre; first <= rest; first++) {
                    ways += dp[first][rest - first];
                }
                dp[pre][first] = ways;
            }
        }

        return dp[1][n];
    }
}


2.3 动态规划优化版本（斜率优化）
public class SplitNumber {
    // n 为正数
    public static int ways(int n) {
        if (n < 0) return 0;

        if (n == 1) return 1;

        int[][] dp = new int[n + 1][n + 1];
    	//pre没有等于0的时候，所以dp表第0行是没有用
        for (int pre = 1; pre <= n; pre++) {
            dp[pre][0] = 1; //第0列
            dp[pre][pre] = 1; //对角线
        }

        //普遍位置
        for (int pre = n - 1; pre >= 1; pre--) {
            for (int rest = pre + 1; rest <= n; rest++) {
                dp[pre][rest] = dp[pre + 1][rest]; //三角下边的位置
                dp[pre][rest] += dp[pre][rest - pre]; //加上左边依赖的第一个位置
            }
        }

        return dp[1][n];
    }
}
————————————————
版权声明：本文为CSDN博主「明朗晨光」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u011386173/article/details/127572646

"""


class Solution():

    def ans1(self, num: int) -> int:
        if num <=0:
            return 0
        if num == 1:
            return 1
        return self.process1(1, num)

    def process1(self, pre: int, rest: int) -> int:
        if rest == 0:
            return 1

        if pre > rest:
            return 0

        if pre == rest:
            return 1

        ways = 0
        for first in range(pre, rest+1):
            ways += self.process1(first, rest - first)

        return ways

    def ans2(self, num: int) -> int:

        if num <= 0:
            return 0

        dp = [[0] * (num+1) for _ in range(num+1)]

        for i in range(num+1):
            dp[i][0] = 1
            dp[i][i] = 1

        for pre in range(num -1, 0, -1):
            for rest in range(pre+1, num+1):

                ways = 0
                for first in range(pre, rest+1):
                    ways += dp[first][rest - first]

                dp[pre][rest] = ways

        return dp[1][num]

    def ans3(self, num: int) -> int:

        if num <= 0:
            return 0

        dp = [[0] * (num+1) for _ in range(num+1)]

        for i in range(num+1):
            dp[i][0] = 1
            dp[i][i] = 1

        for pre in range(num -1, 0, -1):
            for rest in range(pre+1, num+1):

                dp[pre][rest] = dp[pre+1][rest]
                if rest - pre >= 0:
                    dp[pre][rest] += dp[pre][rest-pre]

        return dp[1][num]

import random


S = Solution()

try_times = 100

correct_flag = True
for _ in range(try_times):
    test = random.randint(1, 50)
    # x1 = S.ans1(test)
    x2 = S.ans2(test)
    x3 = S.ans2(test)

    if x3 != x2:
        print(f"test:{test}, x3:{x3}, x2:{x2}")
        correct_flag = False

if correct_flag:
    print("Congratulations! Your answer is perfect!")

print(S.ans3(39))