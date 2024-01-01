
"""
给定一个数组arr，arr代表第i号咖啡机泡一杯咖啡的时间给
定一个正数N，表示N个人等着咖啡机泡咖啡
每台咖啡机只能轮流泡咖啡只有一台咖啡机，一次只能洗一个杯子，时间耗费a，
洗完才能洗下一杯每个咖啡杯也可以自己挥发干净，时间耗费b，咖啡杯可以并行挥发
假设所有人拿到咖啡之后立刻喝干净，返回从开始等到所有咖啡机变干净的最短时间
三个参数 :int[] arr、int N，int a、int b


"""

"""
Java Code 
// 以下为贪心+优良暴力
	public static class Machine {
		public int timePoint;
		public int workTime;

		public Machine(int t, int w) {
			timePoint = t;
			workTime = w;
		}
	}

	public static class MachineComparator implements Comparator<Machine> {

		@Override
		public int compare(Machine o1, Machine o2) {

			return (o1.timePoint + o1.workTime) - (o2.timePoint + o2.workTime);
		}
	}

	// 优良一点的暴力尝试的方法
	public static int minTime1(int[] arr, int n, int a, int b) {
		//建小分堆
		PriorityQueue<Machine> heap = new PriorityQueue<Machine>(new MachineComparator());
		for (int i = 0; i < arr.length; i++) {
			heap.add(new Machine(0, arr[i]));
		}
		int[] drinks = new int[n];
		for (int i = 0; i < n; i++) {
			Machine cur = heap.poll();
			cur.timePoint += cur.workTime;
			drinks[i] = cur.timePoint;
			heap.add(cur);
		}
		return bestTime(drinks, a, b, 0, 0);
	}

	// drinks 所有杯子可以开始洗的时间
	// wash 单杯洗干净的时间（串行）
	// air 挥发干净的时间(并行)
	// free 洗的机器什么时候可用
	// drinks[index.....]都变干净，最早的结束时间（返回）
	public static int bestTime(int[] drinks, int wash, int air, int index, int free) {
		if (index == drinks.length) {
			return 0;
		}
		// index号杯子 决定洗
		int selfClean1 = Math.max(drinks[index], free) + wash;
		int restClean1 = bestTime(drinks, wash, air, index + 1, selfClean1);
		int p1 = Math.max(selfClean1, restClean1);

		// index号杯子 决定挥发
		int selfClean2 = drinks[index] + air;
		int restClean2 = bestTime(drinks, wash, air, index + 1, free);
		int p2 = Math.max(selfClean2, restClean2);
		return Math.min(p1, p2);
	}


"""

"""
python 代码

import heapq

class Machine:
    def __init__(self, time_point, work_time):
        self.time_point = time_point
        self.work_time = work_time

class MachineComparator:
    def __lt__(self, o1, o2):
        return (o1.time_point + o1.work_time) < (o2.time_point + o2.work_time)

def min_time1(arr, n, a, b):
    heap = []
    heapq.heapify(heap)
    for i in range(len(arr)):
        heapq.heappush(heap, Machine(0, arr[i]))

    drinks = [0] * n
    for i in range(n):
        cur = heapq.heappop(heap)
        cur.time_point += cur.work_time
        drinks[i] = cur.time_point
        heapq.heappush(heap, cur)

    return best_time(drinks, a, b, 0, 0)

def best_time(drinks, wash, air, index, free):
    if index == len(drinks):
        return 0

    # Index号杯子决定洗
    self_clean1 = max(drinks[index], free) + wash
    rest_clean1 = best_time(drinks, wash, air, index + 1, self_clean1)
    p1 = max(self_clean1, rest_clean1)

    # Index号杯子决定挥发
    self_clean2 = drinks[index] + air
    rest_clean2 = best_time(drinks, wash, air, index + 1, free)
    p2 = max(self_clean2, rest_clean2)

    return min(p1, p2)

# 示例用法
arr = [3, 1, 4]
n = 3
a = 1
b = 2

result = min_time1(arr, n, a, b)
print(result)


"""

import heapq
from typing import List
class Machine():

    def __init__(self, time_point: int, work_time: int):
        self.time_point = time_point
        self.work_time = work_time

    def __gt__(self, other):
        return (self.time_point + self.work_time) > (other.time_point + other.work_time)

    # def __lt__(self, other):
    #     return (self.timePoint + self.workTime) < (other.timePoint + other.workTime)
        # return self.timePoint > other.timePoint



class Solution():

    def best_time(self, drinks: List, wash: int, air: int, index: int, free: int) -> int:
        if index == len(drinks):
            return 0

        self_clean1 = max(drinks[index], free) + wash
        rest_clean1 = self.best_time(drinks, wash, air, index+1, self_clean1)
        p1 = max(self_clean1, rest_clean1)

        self_clean2 = drinks[index] + air
        rest_clean2 = self.best_time(drinks, wash, air, index+1, free)
        p2 = max(self_clean2, rest_clean2)

        return min(p1, p2)


    def min_time1(self, arr: List, n: int, a: int, b: int):
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, Machine(0, arr[i]))

        drinks = [0] * n

        for i in range(n):
            cur = heapq.heappop(heap)
            cur.time_point += cur.work_time
            drinks[i] = cur.time_point
            heapq.heappush(heap, cur)

        return self.best_time(drinks, a, b, 0, 0)
    def min_time2(self, arr: List, n: int, a: int, b: int):
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, Machine(0, arr[i]))

        drinks = [0] * n

        for i in range(n):
            cur = heapq.heappop(heap)
            cur.time_point += cur.work_time
            drinks[i] = cur.time_point
            heapq.heappush(heap, cur)

        return self.bestTimeDp(drinks, a, b)

    def bestTimeDp(self, drinks: List, wash: int, air: int) -> int:
        maxFree = 0

        for i in range(len(drinks)):
            maxFree = max(maxFree, drinks[i]) + wash

        N = len(drinks)
        dp = [[0] * (maxFree+1) for _ in range(N+1)]

        for i in range(N-1, -1, -1):
            for j in range(maxFree+1):
                self_clean1 = max(drinks[i], j) + wash

                if self_clean1 > maxFree:
                    continue

                rest_clean1 = dp[i + 1][self_clean1]
                p1 = max(self_clean1, rest_clean1)

                self_clean2 = drinks[i] + air
                rest_clean2 = dp[i + 1][j]
                p2 = max(self_clean2, rest_clean2)

                dp[i][j] = min(p1, p2)


        return dp[0][0]



arr = [7, 2, 4, 8, 3]
n = 5
a = 1
b = 8

S = Solution()
# M = Machine(0, arr[0])
# h = []

#
# print(M.timePoint, M.workTime)
result1 = S.min_time1(arr, n, a, b)
result2 = S.min_time2(arr, n, a, b)
print(result1)
print(result2)
#
