class Solution:
    def process(self, nums, idx, pick, rest):
        if idx == len(nums):  # 没数了！！
            return 0 if pick == 0 else -1
        else:  # 还有数
            p1 = self.process(nums, idx + 1, pick, rest)  # 不要这个数
            p2 = -1
            if rest >= nums[idx]:  # 可以要这个数
                next_result = self.process(nums, idx + 1, pick - 1, rest - nums[idx])
                if next_result != -1:
                    p2 = nums[idx] + next_result
            return max(p1, p2)

    def SplitSumClosedSizeHalf(self, nums):
        N = len(nums)
        if N < 2:
            return 0

        arr_sum = sum(nums)
        target_sum = arr_sum // 2

        if N % 2 == 0:
            return self.process(nums, 0, N // 2, target_sum)
        else:
            p1 = self.process(nums, 0, N // 2, target_sum)
            p2 = self.process(nums, 0, (N + 1) // 2, target_sum)
            return max(p1, p2)

# 示例调用
nums_example = [1, 2, 3, 4, 5]
solution = Solution()
result_example = solution.SplitSumClosedSizeHalf(nums_example)
print(result_example)
