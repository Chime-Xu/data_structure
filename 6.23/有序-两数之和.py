""" 第 167 题 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""
from typing import List
# 对撞指针
def towSum3(nums: List, target: int):
    # nums.sort()  #先排序
    left = 0
    right = len(nums) - 1
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            print(left, right)
            left += 1  # 考虑不全面
            right -= 1
        else:
            if curr < target:
                left += 1
            else:
                right -= 1
l3=[1,2,3,4,5]
print(towSum3(l3,7))