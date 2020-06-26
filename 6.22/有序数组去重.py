"""
leetcode第026题数组去重(删除排序数组中的重复项)
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
from typing import List
class Sloution1:
    def quchong(self, nums: List):
        n = len(set(nums))
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                temp = nums[i + 1]
                nums[i + 1:len(nums) - 1] = nums[i + 2:len(nums)]
                nums[-1] = temp
                continue
            else:
                i += 1
        return i + 1

class soulution2:
    def quchong(self, nums: List):
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1
