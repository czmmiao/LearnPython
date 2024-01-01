"""

题目
给定5个参数，N，M，row，col，k。
表示在 N * M的区域上，醉汉Bob初始在(row,col)位置。Bob一共要迈出k步，且每步都会等概率向上下左右四个方向走一个单位。
任何时候Bob只要离开N * M的区域，就直接死亡
求：返回k步之后，Bob还在N*M的区域的概率。
————————————————
版权声明：本文为CSDN博主「善良的Leexx」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43936962/article/details/134219220

public static double livePosibility1(int row, int col, int k, int N, int M) {
        return (double) (process(row, col, k, N, M)) / Math.pow(k, 4);
    }

    public static int process(int row, int col, int rest, int N, int M) {
    	//走出N * M范围，直接狗带
        if (row < 0 || row == N || col < 0 || col == M) {
            return 0;
        }

		//还在范围内，不过剩余步数rest = 0，此时return 1.
        if (rest == 0) {
            return 1;
        }
        int left = process(row - 1, col, rest - 1, N, M);
        int right = process(row + 1, col, rest - 1, N, M);
        int up = process(row, col + 1, rest - 1, N, M);
        int down = process(row, col - 1, rest - 1, N, M);

        return left + right + up + down;
    }

public static double dp(int row, int col, int k, int N, int M) {
        int[][][] dp = new int[N][M][k + 1];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                dp[i][j][0] = 1;
            }
        }
        for (int rest = 1; rest <= k; rest++) {
            for (int r = N - 1; r >= 0; r--) {
                for (int c = M - 1; c >= 0; c--) {
                    dp[r][c][rest] = pick(dp, r - 1, c, rest - 1, N, M);
                    dp[r][c][rest] += pick(dp, r + 1, c, rest - 1, N, M);
                    dp[r][c][rest] += pick(dp, r, c + 1, rest - 1, N, M);
                    dp[r][c][rest] += pick(dp, r, c - 1, rest - 1, N, M);
                }
            }
        }
        return (double)dp[row][col][k] / Math.pow(4,k);
    }

"""

class Solution:

    def liveProbability1(self, row: int, col: int, k: int, N: int, M: int) -> float:
        return self.process1(row, col, k, N, M) / pow(4, k)

    def liveProbability2(self, row: int, col: int, k: int, N: int, M: int) -> float:
        return self.process2(row, col, k, N, M) / pow(4, k)

    def process1(self, row: int, col: int, rest: int, N: int, M: int) -> int:
        if row < 0 or row >= N or col < 0 or col >= M:
            return 0
        if rest == 0:
            return 1

        p1 = self.process1(row, col-1, rest -1, N, M)
        p2 = self.process1(row, col+1, rest -1, N, M)
        p3 = self.process1(row-1, col, rest -1, N, M)
        p4 = self.process1(row+1, col, rest -1, N, M)

        return p1 + p2 + p3 + p4

    def process2(self, r: int, c: int, k: int, N: int, M: int) -> int:

        def pick(dp, row, col, k, N, M):
            if row < 0 or row >= N or col < 0 or col >= M:
                return 0
            else:
                return dp[k][row][col]
        dp = [[[0]*(M) for _ in range(N)] for _ in range(k+1)]
        for i in range(N):
            for j in range(M):
                dp[0][i][j] = 1

        for rest in range(1, k+1):
            for row in range(N):
                for col in range(M):
                    p1 = pick(dp, row, col - 1, rest - 1, N, M)
                    p2 = pick(dp, row, col + 1, rest - 1, N, M)
                    p3 = pick(dp, row - 1, col, rest - 1, N, M)
                    p4 = pick(dp, row + 1, col, rest - 1, N, M)
                    dp[rest][row][col] = p1 + p2 + p3 + p4

        return dp[k][r][c]

S = Solution()


import random

correct_flag = True
try_times = 2000

for i in range(try_times):
    row = random.randint(1, 5)
    col = random.randint(1, 5)
    k = random.randint(1, 5)
    N = random.randint(6, 10)
    M = random.randint(6, 10)


    try:
        x1 = S.liveProbability1(row, col, k, N, M)
        x2 = S.liveProbability2(row, col, k, N, M)


        if x1 != x2:
            print(f"row : {row}, col : {col}, k : {k},  N : {N}, M: {M}")
            print(f"x1:{x1}, x2:{x2}")
            correct_flag = False
    except:
        print(f"row : {row}, col : {col}, k : {k},  N : {N}, M: {M}")


if correct_flag:
    print("Congratulations! The answer is perfect!")

# print(f"{row}: row, {col}: col, {k}: k, {N}: N, {M}: M")
# x2 = S.liveProbability2(row, col, k, N, M)