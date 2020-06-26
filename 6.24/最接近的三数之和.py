""" 第 16 题  给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。"""

from typing import List

def threeSumClosest(nums: List,target: int) -> int:
    #有序
    nums.sort()
    #初始化
    res=nums[0]+nums[1]+nums[2]
    min=abs(res-target)
    #固定C 位
      #  nums = [-4,-1,1,2]
    for i in range(len(nums)-2):
        left=i+1
        right=len(nums)-1
        #当前nums[i]情况下,搜索最接近的组合
        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            #比较sums与目标target的距离与之前最近的距离,如果更近则更新
            if abs(sum-target)<min:
                min=abs(sum-target)
                res=sum
            if sum>target:
                right -=1
            elif sum<target:
                left +=1
            #如果sum与target相等,则说明距离为0,为最接近的数
            else:
                return sum
    return res
nums = [-1,2,1,-4]
print(threeSumClosest(nums,1))