"""
假设有排成一行的N个位置，记为1~N，N 一定大于或等于 2
开始时机露人在其中的M位置上(M 一定是 1~N 中的一个)
如果机器人来到1位置。那么下一步只能往右来到2位置:
如果机器人来到N位置，那么下一步只能往左来到 N-1 位置 ;
如果机器人来到中间位置，那么下一步可以往左走或者往右走 :
规定机器人必须走 K步，最终能来到P位置(P也是1~N中的一个)的方法有多少种
给定四个参数N、M、K、P

返回方法数。

"""

def Ways1(N: int, M: int, K: int, P:int) -> int:

    return dp1(M, K, P, N)

def dp1(cur: int, rest: int, aim: int, N: int) -> int:

    if rest == 0:
        if cur == aim:
            return 1
        else:
            return 0
    elif rest > 0:
        if cur == 1:
            return dp1(cur+1, rest-1, aim, N)
        elif cur == N:
            return dp1(cur-1, rest-1, aim, N)
        elif cur > 1 and cur < N:
            return dp1(cur-1, rest-1, aim, N) + dp1(cur+1, rest-1, aim, N)

def Ways2(N: int, M: int, K: int, P:int) -> int:

    memo = [[None for _ in range(K+1)] for _ in range(N+1)]
    return dp2(M, K, P, N, memo)

def dp2(cur: int, rest: int, aim: int, N: int, memo: list) -> int:

    if rest == 0:
        if cur == aim:
            return 1
        else:
            return 0

    if memo[cur][rest] != None:
        return memo[cur][rest]

    elif rest > 0:
        if cur == 1:
            memo[cur][rest] = dp2(cur+1, rest-1, aim, N)
            return dp2(cur+1, rest-1, aim, N)
        elif cur == N:
            memo[cur][rest] = dp2(cur-1, rest-1, aim, N)
            return dp2(cur-1, rest-1, aim, N)
        elif cur > 1 and cur < N:
            memo[cur][rest] = dp1(cur - 1, rest - 1, aim, N) + dp1(cur + 1, rest - 1, aim, N)
            return dp1(cur-1, rest-1, aim, N) + dp1(cur+1, rest-1, aim, N)



def Ways3(N: int, M: int, K: int, P:int) -> int:

    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    dp[P][0] = 1
    for rest in range(1, K+1):
        dp[1][rest] = dp[2][rest-1]
        for cur in range(2, N):
            dp[cur][rest] = dp[cur-1][rest-1] + dp[cur+1][rest-1]
        dp[N][rest] = dp[N-1][rest-1]

    return dp[M][K]

result1 = Ways1(7, 4, 9, 5)
print(result1)
result2 = Ways2(4, 2, 4, 4)
print(result2)
result2 = Ways2(7, 4, 9, 5)
print(result2)
result3 = Ways3(7, 4, 9, 5)
print(result3)
result3 = Ways3(4, 2, 4, 4)
print(result3)