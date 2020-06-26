"""leetcode 283 - 移动零
问题描述
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
思路
i 指针用于存放非零元素
j 指针用于遍历寻找非零元素
（注：j 指针找到一个非零元素后，nums[i] 的位置 i++，用于下一个 j 指针找到的非零元素）
j 指针遍历完后，最后 nums 数组还有空位置，存放 0 即可"""
from typing import List
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         index=0
#         for i in range(len(nums)):
#             if nums[i]!=0:
#                 nums[i],nums[index]=nums[index],nums[i]
#                 index+=1
#         # return nums
#         print(nums)
# if __name__ == '__main__':
#     a=Solution()
#     a.moveZeroes([1,2,0,3,0,5,6,0])

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow,fast=0,0
        #[0,1,2,2,3,0,4,2]
        while fast<len(nums):
            if nums[fast]==0:
                fast +=1
            else:
                # nums[slow],nums[fast]=nums[fast],nums[slow]  #直接交换,不需要后面的遍历
                nums[slow]=nums[fast]
                slow +=1  #慢指针前进前提  快指针发现不同值
                fast +=1
        for i in range(slow,len(nums)): # 未替换,就需要遍历将最后都替换为0
            nums[i]=0

def moveZeroes(nums):
    slow, fast = 0, 0
    # [0,1,2,2,3,0,4,2]
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow],nums[fast]=nums[fast],nums[slow]  #直接交换,不需要后面的遍历
            # nums[slow] = nums[fast]
            slow += 1  # 慢指针前进前提  快指针发现不同值
            fast += 1
    # for i in range(slow, len(nums)):  # 未替换,就需要遍历将最后都替换为0
    #     nums[i] = 0
        print(nums)
nums=[1,0,2,0,3]
print(moveZeroes(nums))
