"""
问题描述：给出3个参数，N,M,K,怪兽有N滴血，等着英雄来砍自己，英雄每一次打击，都会让怪兽流失[0~M]的血量，到底流失多少？每一次在[0~M]上等概率的获取一个值，求K次打击之后，英雄把怪兽砍死的概率

例如：

int N =  6;
int M = 3;
int K =  5;
————————————————
版权声明：本文为CSDN博主「nandao158」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/nandao158/article/details/118674275


public class NanDaoKillMonster {
    public static void main(String[] args) {
        int N =  6;
        int M = 3;
        int K =  5;
        double ans1 = killMonster(N, M, K);
        double ans2 = killDp1(N, M, K);
        double ans3 = killDp2(N, M, K);
        System.out.println("ans1:"+ans1+";ans2:"+ans2+";ans3:"+ans3);
    }



    private static double killMonster(int N, int M, int K) {
        if(N < 1 || M < 1 || K < 1){//边界验证
            return 0;
        }
        long all = (long) Math.pow(M + 1,K);//理想情况下打击的次数
        long kill = killProcess(K,M,N);//kill怪兽的次数
        //两者相比就是kill的概率
        return (double)((double)kill/(double)all);
    }

    private static long killProcess(int times, int M, int hp) {
        if(times == 0){//还剩0次时，验证怪兽是否打死
            return hp <= 0? 1:0;
        }
        if(hp <= 0){//如果怪兽已经没血了，直接返回此种情况kill的次数
            return (long)Math.pow(M + 1,times);
        }
        int ways = 0;
        for(int i = 0;i <= M;i++){
            //每次次数减 1，血滴数减 i,进行暴力递归
            ways +=killProcess(times -1,M,hp - i);
        }
        return ways;
    }
}

public class NanDaoKillMonster {
    public static void main(String[] args) {
        int N =  6;
        int M = 3;
        int K =  5;
        double ans1 = killMonster(N, M, K);
        double ans2 = killDp1(N, M, K);
        double ans3 = killDp2(N, M, K);
        System.out.println("ans1:"+ans1+";ans2:"+ans2+";ans3:"+ans3);
    }



    private static double killDp1(int N, int M, int K) {
        if(N < 1 || M < 1 || K < 1){
            return 0;
        }
        long all = (long)Math.pow(M + 1,K);//理想情况下打击的次数
        long[][] dp = new long[K+ 1][N + 1];
        dp[0][0] = 1;//初始化次数
        for(int times = 1;times <= K;times++){
            //如果怪兽已经没血了，直接返回此种情况kill的次数
            dp[times][0] = (long)Math.pow(M + 1,times);
            for(int hp = 1;hp <= N;hp++){//遍历怪兽的血滴
                long ways = 0;
                /**
                 * [0~M]比如 M = 3,
                 * dp[5][10] 依赖dp[4][10]，dp[4][9]，dp[4][8]，dp[4][7],
                 * 因此有下面的循环依赖
                 */
                for(int i = 0;i <= M;i++){
                    if(hp - i >= 0){
                        //如果还有血滴，继续叠加
                        ways += dp[times - 1][hp - i];
                    }else {
                        //如果怪兽已经没血了，直接返回此种情况kill的次数
                        ways += (long)Math.pow(M + 1,times - 1);
                    }
                }
                dp[times][hp] = ways;
            }
        }
        long kill = dp[K][N];//kill怪兽的次数
        //两者相比就是kill的概率
        return (double)((double)kill/(double) all);
    }
}


public class NanDaoKillMonster {
    public static void main(String[] args) {
        int N =  6;
        int M = 3;
        int K =  5;
        double ans1 = killMonster(N, M, K);
        double ans2 = killDp1(N, M, K);
        double ans3 = killDp2(N, M, K);
        System.out.println("ans1:"+ans1+";ans2:"+ans2+";ans3:"+ans3);
    }

    private static double killDp2(int N, int M, int K) {
        if(N < 1 || M < 1 || K < 1){
            return 0;
        }
        long all = (long)Math.pow(M + 1,K);
        long[][] dp = new long[K + 1][N + 1];
        dp[0][0] = 1;
        for(int times = 1;times <= K;times++){
            dp[times][0] = (long)Math.pow(M + 1,times);
            /**
             * 比如：
             * [0~M]假设 M = 7,
             * dp[5][10] 依赖 dp[4][10 ~ 3]八个位置的数值
             * dp[5][11] 依赖 dp[4][11 ~ 4]八个位置的数值 ，又等于dp[5][10] + dp[4][11] - dp[4][3]
             * 因此有下面的循环依赖
             * 总结通用公式：
             *      dp[i][j-1] = dp[i-1][j-1 ~ j-1-M]
             *      dp[i][j] = dp[i-1][j ~ j-M]
             *      dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1-M]
             *      前提是血量 j>0,如果 j < 0,此种次数(M + 1)的 i即times 次方
             */
            for(int hp = 1;hp <= N;hp++){
                dp[times][hp] = dp[times - 1][hp] + dp[times][hp - 1];
                if(hp - 1 - M >= 0){
                    dp[times][hp] -= dp[times -1][hp - 1 -M];
                }else {
                    dp[times][hp] -= Math.pow(M + 1,times - 1);
                }
            }
        }
        long kill = dp[K][N];
        //两者相比就是kill的概率
        return (double)((double)(kill)/(double)(all));
    }
}

"""

class Solution():

    def ans1(self, N: int, M: int, K:int) -> float:
        if M <= 0 or N <= 0 or K <= 0:
            return 0

        all_times = pow(M+1, K)
        kill_times = self.process1(N, M, K)

        return kill_times/all_times

    def process1(self, hp: int, M: int, times: int) -> int:

        if times == 0:
            return 1 if hp<=0 else 0

        if hp <= 0:
            return pow(M+1, times)
        ways = 0
        for i in range(M+1):
            ways += self.process1(hp -i, M, times-1)

        return ways

    def dp1(self, N: int, M: int, K: int) -> float:
        if M <= 0 or N <= 0 or K <= 0:
            return 0
        all_times = pow(M+1, K)
        dp = [[0] * (K+1) for _ in range(N + 1)]

        dp[0][0] = 1

        for times in range(1, K+1):
            dp[0][times] = pow(M+1, times)

            for hp in range(1, N+1):
                ways = 0
                for m in range(M+1):
                    if hp - m >=0:
                        ways += dp[hp-m][times-1]
                    else:
                        ways += pow(M+1, times-1)

                dp[hp][times] = ways

        return dp[N][K]/all_times

    def dp2(self, N: int, M: int, K: int) -> float:
        if M <= 0 or N <= 0 or K <= 0:
            return 0
        all_times = pow(M+1, K)
        dp = [[0] * (K+1) for _ in range(N + 1)]

        dp[0][0] = 1

        for times in range(1, K+1):
            dp[0][times] = pow(M+1, times)

            for hp in range(1, N+1):
                dp[hp][times] = dp[hp][times-1] + dp[hp-1][times]
                if hp >= M+1:
                    dp[hp][times] -= dp[hp-M-1][times-1]
                else:
                    dp[hp][times] -= pow(M+1, times-1)

        return dp[N][K]/all_times






N =  6
M = 3
K =  5
S = Solution()
print(S.ans1(N, M, K))
print(S.dp1(N, M, K))
print(S.dp2(N, M, K))