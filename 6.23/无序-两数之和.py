""" 第 1 题  给定一个整数数组 nums (无序数组) 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。"""

from typing import List

# 暴力解决  空间复杂度 O(1)  时间复杂度 O(n2次方)
def towSum1(nums: List, target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return False
l1=[1,2,4,5,3]
print(towSum1(l1,7))

# 字典存储   空间复杂度 O(n)   时间复杂度 O(n)
def towSum2(nums: List, target: int):
    nums_dict={}  #字典存放  (数值:下标)
    for i in range(len(nums)):
        temp=target-nums[i]  #temp存放差值
        if temp in nums_dict:
            return [i,nums_dict[temp]]
        else:
            nums_dict[nums[i]] = i
l2=[1,2,3,5,4]
print(towSum2(l2,7))