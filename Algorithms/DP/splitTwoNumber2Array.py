"""
给定一个正数数组arr，请把arr中所有的数分成两个集合如果arr长度为偶数，
两个集合包含数的个数要一样多如果arr长度为奇数，两个集合包含数的个数必须只差一个请尽量让两个集合的累加和接近

返回:
最接近的情况下，较小集合的累加和


    /**
     * 递归拆分数组
     * @param arr
     * @return
     */
    public static int right(int[] arr) {
        if (arr == null || arr.length < 2){
            return 0;
        }
        int sum  = 0;
        for (int a : arr){
            sum += a;
        }
        //长度是偶数时,只有一个选择
        if ((arr.length & 1) == 0){
            return process(arr,0,sum / 2,arr.length / 2);
        }else{
            //长度为奇数时,讨论两种情况
            return Math.max(process(arr,0,sum / 2,arr.length / 2),process(arr,0,sum / 2,arr.length / 2 + 1));
        }

    }

    /**
     * 递归
     * @param arr 数组
     * @param index 下标
     * @param rest 累加和的目标值
     * @param size 需要选择的元素个数
     * @return
     */
    public static int process(int[] arr,int index,int rest,int size){
        //base case 越界时,没有可选择的数了
        if (index == arr.length){
            //如果到最后一个位置,需要选择的元素,刚好选完,就没有可选了,返回0.
            // size 不等于0,之前的选择是无效的,返回-1 标记
            return size == 0 ? 0 : -1;
        }
        //当前元素不选择时,index + 1 ,去下一个位置选,
        int p1 = process(arr,index + 1,rest,size);
        //无效值时我们用-1 标记,因此p2 也要用-1 初始化,避免比较结果时产生影响
        int p2 = -1;
        if (arr[index] <= rest){
            //选择时,去下一个位置继续选择index + 1
            //累加和减去已经选择的rest - arr[index]
            //需要选择的元素个数减一
           int next =  process(arr,index + 1,rest - arr[index],size - 1);
           if (next != -1){
               p2 = arr[index] + next;
           }
        }
        return Math.max(p1,p2);
    }


    /**
     * 动态规划
     * @param arr
     * @return
     */
    public static int dp(int[] arr) {
        if (arr == null || arr.length < 2) {
            return 0;
        }
        int sum = 0;
        for (int a : arr) {
            sum += a;
        }
        int binarySum = sum / 2;
        int N  = arr.length;
        int M = (N + 1)/2;
        //动态规划表
        int[][][]dp = new int[N + 1][M + 1][binarySum + 1];
        //先把值都初始化为-1
        for (int i = 0; i <= N;i++){
            for (int j = 0;j <= M;j++){
                for (int k = 0;k <= binarySum;k++){
                    dp[i][j][k] = -1;
                }
            }
        }

        //根据base case 初始化已经确定的值
        for (int k = 0;k <= binarySum;k++){
            dp[N][0][k] = 0;
        }
        //递归过程改写
        for (int i = N - 1;i >= 0;i--){
            for (int j = 0;j <= M;j++){
                for (int k = 0 ; k <= binarySum;k++){
                    int p1 = dp[i+1][j][k];
                    int p2 = -1;
                    if (j - 1 >= 0 && arr[i] <= k){
                        //选择时,去下一个位置继续选择index + 1
                        //累加和减去已经选择的rest - arr[index]
                        //需要选择的元素个数减一
                        int next =  dp[i+1][j - 1][k - arr[i]];
                        if (next != -1){
                            p2 = arr[i] + next;
                        }
                    }
                    dp[i][j][k] = Math.max(p1,p2);
                }
            }
        }
        //数组长度不同时的情况讨论
        if (N % 2 == 0){
            return dp[0][N / 2][binarySum];
        }else{
            return Math.max(dp[0][N / 2][binarySum],dp[0][N / 2 + 1][binarySum]);
        }

    }


"""

from typing import List
class Solution():

    def SplitSumClosedSizeHalf(self, arr: List) -> int:
        arr_sum = sum(arr)
        arr_len = len(arr)

        if arr_len%2 == 0:
            return self.process1(arr, 0, arr_sum//2, arr_len//2)
        elif arr_len%2 == 1:
            return max(self.process1(arr, 0, arr_sum//2, arr_len//2), self.process1(arr, 0, arr_sum//2, arr_len//2+1))


    def process1(self, arr: List, idx: int, arr_sum: int, size: int) -> int:

        if idx == len(arr):
            return 0 if size == 0 else -1

        p1 = self.process1(arr, idx + 1, arr_sum, size)

        p2 = -1
        if arr_sum >= arr[idx]:
            next = self.process1(arr, idx + 1, arr_sum - arr[idx], size -1)
            if next != -1:
                p2 = next + arr[idx]

        return max(p1, p2)
    def SplitSumClosedSizeHalf2(self, arr: List) -> int:

        rest = sum(arr)//2
        N = len(arr)
        M = -(-N//2)

        dp = [[[-1]*(M + 1) for _ in range(rest + 1)] for _ in range(N + 1)]


        for r in range(rest + 1):
            dp[N][r][0] = 0

        for n in range(N-1, -1, -1):
            for r in range(rest + 1):
                for m in range(M + 1):
                    p1 = dp[n+1][r][m]
                    p2 = -1
                    if r >= arr[n] and m-1>=0:
                        next = dp[n+1][r-arr[n]][m-1]
                        if next != -1:
                            p2 = next + arr[n]
                    dp[n][r][m] = max(p1, p2)

        if N % 2 == 0:
            return dp[0][rest][N//2]
        elif N % 2 == 1:
            return max(dp[0][rest][N//2],
                       dp[0][rest][N//2 + 1])



import random

def generate_array(max_len, min_value, max_value):
    size = random.randint(1, max_len)
    result = [[0, 0] for _ in range(size)]
    for i in range(size):
        v1 = random.randint(min_value, max_value)
        v2 = random.randint(min_value, max_value)
        if v1 == v2:
            result[i][0] = v1
            result[i][1] = v1 + 1
        else:
            result[i][0] = min(v1, v2)
            result[i][1] = max(v1, v2)
    return result


if __name__ == "__main__":

    max_len = 20
    max_value = 50
    test_time = 30
    a = Solution()
    for i in range(test_time):
        length = random.randint(0, max_len)
        array = [random.randint(0, max_value) for _ in range(length)]

        ans1 = a.SplitSumClosedSizeHalf(array)
        ans2 = a.SplitSumClosedSizeHalf2(array)
        if ans1 != ans2:
            print("error")
            exit(-1)
    print("finish!")


arr = [1,2,3,4, 5]
S = Solution()
ans = S.SplitSumClosedSizeHalf2(arr)
print(ans)