# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2025-01-19 12:21:07
# @Description: Permuation Sum


import copy
class Solution:
    def combsum(self, nums: list[int], n:int, target: int, arr: list[int], res: list[list[int]]):
        if target == 0:
            res.append(copy.deepcopy(arr))
            return

        if target < 0:
            return

        for i in range(n):
            arr.append(nums[i])
            target -= nums[i]
            self.combsum(nums, len(nums), target, arr, res)
            ele = arr.pop()
            target += ele

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []    
        self.combsum(candidates, len(candidates), target, [], res)
        return res
    
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
