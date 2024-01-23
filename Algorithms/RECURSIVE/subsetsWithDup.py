
"""

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的组合
答案 不能 包含重复的组合。返回的答案中，组合可以按 任意顺序 排列
注意其实要求返回的不是子集，因为子集一定是不包含相同元素的，要返回的其实是不重复的组合
比如输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
测试链接 : https://leetcode.cn/problems/subsets-ii/

"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        N = len(nums)
        self.process1(nums, 0, [0] * N, N, ans)
        return ans

    def process1(self, nums: List, idx: 0, path: List, size: int, ans: List) -> List[List[int]]:

        if idx == len(nums):
            cur = path[:size]
            ans.append(cur[:])
        else:
            j = idx + 1
            while j < len(nums) and nums[idx] == nums[j]:
                j += 1

            self.process1(nums, j, path, size, ans)

            for k in range(idx, j):
                path[size] = nums[k]
                self.process1(nums, idx, path, size+1, ans)

