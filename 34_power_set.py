# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2025-01-19 10:48:29
# @Description: Power Set
'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]
 

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
'''

import copy

def powersetbuilder(nums: list[int], powerarr: list[int], index: int, n: int, finalarr: list[list[int]])-> None:
    # print(index, nums,powerarr,type(nums),type(powerarr))
    if(index == n - 1):
        finalarr.append(copy.deepcopy(powerarr))
        return
    index += 1
    powersetbuilder(nums, powerarr, index, n, finalarr)
    powerarr.append(nums[index])
    powersetbuilder(nums, powerarr, index, n, finalarr)
    powerarr.pop()
    return


def genpowerset(nums : list[int], powersetarr: list[list[int]]) -> None:
    arr = list()
    powersetbuilder(nums, [], -1, len(nums), powersetarr)
    print(powersetarr)


def genpoweset2(num: list[int]) -> list[list[int]]:
    l = len(num)
    n = pow(2,l)
    res = []
    for i in range(n):
        subset = []
        for j in range(l):
            if (i & 1 << j):
                subset.append(num[j])
        res.append(subset)
    return res
def main():
    print("Hello, World!")
    psarr = []
    genpowerset([1,2,3],psarr)
    print(genpoweset2([1,2,3]))


if __name__ == "__main__":
    main()
