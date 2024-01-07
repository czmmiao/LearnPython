"""
题目一、
给定一个正数数组arr，
请把arr中所有的数分成两个集合，尽量让两个集合的累加和接近
返回：
最接近的情况下，较小集合的累加和
package class23;

/**
 * 给定一个正数数组arr，
 * 请把arr中所有的数分成两个集合，尽量让两个集合的累加和接近
 * 返回：
 * 最接近的情况下，较小集合的累加和
 */
public class SplitSumClosed {

    //方法一：暴力递归
    public static int right(int[] arr){
        //边界判断 少于2个 就不符合题意
        if(arr ==  null || arr.length < 2) return 0;

        //需要分成两个集合，且累加和接近 那么就可以判断一个边界范围 是不超过全部数和的一半
        int sum = 0;
        for(int a:arr){
            sum += a;
        }

        //调用递归函数 从数组0开始，到sum/2;
        return process(arr, 0, sum/2);
    }

    /**
     * 对数组[index...]的数据划分靠近rest当前剩余累加和数，且不超过rest 返回该最接近且不超过rest的累加和
     * @param arr
     * @param index
     * @param rest
     * @return
     */
    public static int process(int[] arr, int index, int rest){
        //base case: 当前来到越界数组 没有元素了 那么就表示到底 直接返回0
        if(index == arr.length) return  0;

        //不越界 表示还有数，那么就分析情况，取该数与不取两种情况
        //1.当前index 不累加 那么就返回 下一个位置 index+1 位置   rest不需要减，因为没有选择就不影响
        int p1 = process(arr,index+1,rest);

        //2.当前index 累加，需要先判断是否越界 就是当前剩余数rest 减完arr[index]值要大于等于0 因为我们要求的是较小集合
        int p2 = 0;
        if(arr[index] <= rest){
            p2 = process(arr, index+1,rest-arr[index]);
        }
        return Math.max(p1,p2);    //两者情况都是符合接近且较小的 但是要取更接近那肯定是较大的更接近中间值的
    }


    //方法二：动态规划
    public static int dp(int[] arr){
        if(arr == null || arr.length < 2) return 0;

        //分析递归可变参数 index  范围0-arr.length   rest 范围0-sum/2
        int n = arr.length;
        int sum = 0;
        for(int num:arr){
            sum+=num;
        }
        //求和接近 所以是总和一半
        sum /= 2;
        int[][] dp = new int[n+1][sum+1];
        //base case 越界index == arr.length 返回0 初始化即为0 不需要处理 完成dp[n] 最后一行的赋值
        //分析依赖 index 依赖 index+1 也就是上一行依赖下一行 所以从倒数第二行开始往上赋值
        for(int index = n-1;index>=0;index--){
            for(int rest = 0; rest <= sum ; rest++){

            //不越界 表示还有数，那么就分析情况，取该数与不取两种情况
            //1.当前index 不累加 那么就返回 下一个位置 index+1 位置   rest不需要减，因为没有选择就不影响
            int p1 = dp[index+1][rest];

            //2.当前index 累加，需要先判断是否越界 就是当前剩余数rest 减完arr[index]值要大于等于0 因为我们要求的是较小集合
            int p2 = 0;
            if(arr[index] <= rest){
                p2 = dp[index+1][rest-arr[index]];
            }
            dp[index][rest] = Math.max(p1,p2);    //两者情况都是符合接近且较小的 但是要取更接近那肯定是较大的更接近中间值的
            }
        }
        return dp[0][sum];     //最后返回递归调用的主函数的位置 0位置开始 在总数一半的位置
    }

    public static int[] randomArray(int len, int value) {
        int[] arr = new int[len];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * value);
        }
        return arr;
    }

    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int maxLen = 20;
        int maxValue = 50;
        int testTime = 10000;
        System.out.println("测试开始");
        for (int i = 0; i < testTime; i++) {
            int len = (int) (Math.random() * maxLen);
            int[] arr = randomArray(len, maxValue);
            int ans1 = right(arr);
            int ans2 = dp(arr);
            if (ans1 != ans2) {
                printArray(arr);
                System.out.println(ans1);
                System.out.println(ans2);
                System.out.println("Oops!");
                break;
            }
        }
        System.out.println("测试结束");
    }

}
题目
————————————————
版权声明：本文为CSDN博主「studyday1」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/studyday1/article/details/129998800

"""

from typing import List

class Solution():
    def ans1(self, arr: List) -> int:

        if len(arr) == 0 or len(arr) <2:
            return 0
        arr_sum = sum(arr)
        return self.process1(arr, 0, arr_sum//2)

    def process1(self, arr: List, idx: int, rest: int) -> int:

        N = len(arr)

        if idx == N:
            return 0

        p1 = self.process1(arr, idx+1, rest)
        p2 = 0
        if arr[idx] <= rest:
            p2 = arr[idx] + self.process1(arr, idx+1, rest - arr[idx])

        return max(p1, p2)

    def process2(self, arr: List):
        if not arr or len(arr) < 2:
            return 0

        arr_sum = sum(arr)

        arr_sum = arr_sum//2
        N = len(arr)
        dp = [[0] * (arr_sum+1) for _ in range(N+1)]

        for idx in range(N-1, -1, -1):
            for rest in range(arr_sum+1):
                p1 = dp[idx+1][rest]
                p2 = 0
                if arr[idx] <= rest:
                    p2 = arr[idx] + dp[idx+1][rest - arr[idx]]

                dp[idx][rest] = max(p1, p2)

        return dp[0][arr_sum]



max_len = 20
max_value = 50
test_time = 300
print("测试开始")

import random

S = Solution()


for _ in range(test_time):
    length = random.randint(0, max_len)
    array = [random.randint(0, max_value) for _ in range(length)]
    ans1 = S.ans1(array)
    ans2 = S.process2(array)

    if ans1 != ans2:
        print(array)
        print(ans1)
        print(ans2)
        print("Oops!")
        break

print("测试结束")