"""
51. N 皇后
困难
相关标签
相关企业
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。



示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]


https://leetcode.cn/problems/n-queens/description/


1.暴力解法
package com.harrison.class12;

public class Code08_NQueens {
	// 0~i-1行的皇后位置都摆放好了，不用再考虑，并且符合要求：不共行、不共列、不共斜线
	// i	表示当前来到第i行摆皇后
	// record[0~i-1]	存放摆好的记录
	// record[0]=3  ->	第0行皇后摆在第3列
	// n	表示一共有多少行（0~n-1行），如果来到n行就越界了
	// 在[0~i-1]行皇后都摆好的情况下，
	// 返回i及其后面行数摆放有效的方式有多少种（整个棋盘都摆好）
	public static int process1(int i,int[] record,int n) {
		// 如果i来到终止行，说明之前行数的摆放都有效，
		// 返回一种合理的摆放方式
		if(i==n) {
			return 1;
		}
		// 如果i没有到终止行，那么当前行可以摆
		int ans=0;
		// 尝试i行上所有的列（0~n-1列）
		// 如果当前i行的皇后，放在第j列，
		// 不会和之前行（0~i-1行）的皇后冲突（不共行&&不共列&&不公斜线）
		// 那放第j列可以，认为有效，接着去i+1行递归
		// 否则，无效，放下一列
		for(int j=0; j<n; j++) {
			if(isValid(record, i, j)) {// record记录的是0~i-1行皇后的位置
				record[i]=j;// 第i行的皇后在第j列
				ans+=process1(i+1, record, n);
				// 因为在每一行都是直接改要放的列数，所以无需恢复现场
			}
		}
		return ans;
	}

	// record[0~i-1]的皇后需要看，第i行的皇后不需要
	// 返回第i行皇后放在了第j列是否有效
	public static boolean isValid(int[] record,int i,int j) {
		for(int k=0; k<i; k++) {// 0~i-1行的某一行的皇后，假设是第k行的皇后
			if(record[k]==j || (Math.abs(record[k]-j)==Math.abs(i-k))) {
				return false;
			}
		}
		return true;
	}

	public static int nums1(int n) {
		if(n<1) {
			return 0;
		}
		int[] record=new int[n];// record[i] i行的皇后 放在了第几列
		return process1(0, record, n);
	}

	public static int nums2(int n) {
		if(n<1 || n>32) {
			return 0;
		}
		// n==8 limit最右边8个1，其余全是0
		// n==9	limit最右边9个1，其余全是0
		// n==32 最右边32位全是1 -> 十进制-1
		// n!=32 1左移n位再减一
		// 比如n==8 limit=100000000-00000001 -> 11111111
		int limit=n==32?-1:((1<<n)-1);
		// 一开始第0行的时候，没有任何限制
		return process2(limit, 0, 0, 0);
	}

	// limit 划定了问题的规模，是固定不变的参数
	public static int process2(int limit,int columnLimit,int leftLimit,int rightLimit) {
		if(columnLimit==limit) {// base case
			return 1;
		}
		// pos 当前行可以放皇后的位置 1：不能放	0：可以放
		// (columnLimit | leftLimit | rightLimit ) 总限制
		// 为什么要 & limit
		// 1）~(columnLimit | leftLimit | rightLimit ) 左侧的一坨0取反后变成1会干扰
		// 2）左斜线限制会越界，右斜线不会
		int pos=limit&(~(columnLimit | leftLimit | rightLimit ));
		int ans=0;
		int mostRightOne=0;
		// 尝试pos上的每一个1
		while(pos!=0) {
			mostRightOne=pos & ((~pos)+1);
			pos=pos-mostRightOne;
			ans+=process2(limit,
						  columnLimit | mostRightOne,
						  (leftLimit | mostRightOne)<<1,
						  (rightLimit | mostRightOne)>>>1);
		}
		return ans;
	}

	public static void main(String[] args) {
		int n=13;
		long start=System.currentTimeMillis();
		System.out.println(nums1(n));
		long end=System.currentTimeMillis();
		System.out.println("cost time："+(end-start)+"ms");

		start=System.currentTimeMillis();
		System.out.println(nums2(n));
		end=System.currentTimeMillis();
		System.out.println("cost time："+(end-start)+"ms");
	}
}


可以看出位运算是最快的方法

和普通算法一样，这是一个递归过程，程序一行一行地寻找可以放皇后的地方。过程带三个参数，row、ld和rd，分别表示在纵列和两个对角线方向的限制条件下这一行的哪些地方不能放。我们以6×6的棋盘为例，看看程序是怎么工作的。假设现在已经递归到第四层，前三层放的子已经标在左图上了。红色、蓝色和绿色的线分别表示三个方向上有冲突的位置，位于该行上的冲突位置就用row、ld和rd中的1来表示。把它们三个并起来，得到该行所有的禁位，取反后就得到所有可以放的位置（用pos来表示）。前面说过-a相当于not a + 1，这里的代码第6行就相当于pos and (not pos + 1)，其结果是取出最右边的那个1。这样，p就表示该行的某个可以放子的位置，把它从pos中移除并递归调用test过程。注意递归调用时三个参数的变化，每个参数都加上了一个禁位，但两个对角线方向的禁位对下一行的影响需要平移一位。最后，如果递归到某个时候发现row=111111了，说明六个皇后全放进去了，此时程序从第1行跳到第11行，找到的解的个数加一。
————————————————
版权声明：本文为CSDN博主「chroje」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/chroje/article/details/79478114


"""

from typing import List


class Solution():
    def isValidPlace(self, record: List, i: int, j: int) -> bool:

        for k in range(i):
            if record[k] == j or (abs(k-i) == (abs(record[k]-j))):
                return False
        return True
    def ans1(self, n: int) -> int:
        if n < 1:
            return 0

        record = [0] * n
        return self.process1(0, record, n)

    def process1(self, idx, record, n):
        if idx == n:
            return 1

        ans = 0

        for j in range(n):
            if self.isValidPlace(record, idx, j):
                record[idx] = j
                ans += self.process1(idx+1, record, n)

        return ans


S = Solution()
print(S.ans1(10))