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