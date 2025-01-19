# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2025-01-18 23:43:16
# @Description: Permutations of a list of unique integers

import copy

def getperm(arr: list[int], currlist: list[int], permlist: list[list[int]], n: int) -> None:
    if(n == 0):
        permlist.append(copy.deepcopy(currlist))
        return
    for i in range(n):
        ele = arr.pop(i)
        currlist.append(ele)
        getperm(arr,currlist,permlist,len(arr))
        currlist.pop()
        arr.insert(i,ele)
    
def findperm(arr: list[int]):
    finallist = []
    getperm(arr, [], finallist, len(arr))
    print(finallist)


def main():
    print("Hello, World!")
    findperm([1,2,3])
    findperm([1,2,3,4,5])
    findperm([1,3])


if __name__ == "__main__":
    main()
