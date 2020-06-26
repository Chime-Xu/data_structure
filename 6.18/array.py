"""
:Author:  XuLing
:Create:  2020/6/19 10:17
:Github:  https://github.com/XXX
Copyright (c) 2020, XuLing Group All Rights Reserved.
"""
# zs 文档注释


class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        """
        :param index: 插入值的索引
        :type index: int
        :param element: 插入的值
        :type element: any
        :return:
        :rtype:
        """
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):  # 包头不包尾
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        for i in range(index, self.size, 1):
            self.array[i] = self.array[i + 1]  # 要触发扩容后删除
        self.size -= 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i], end='->')


if __name__ == '__main__':
    array = Array(3)
    array.insert(0, 1)
    array.insert(1, 2)
    array.insert(2, 3)
    array.insert(3, 4)
    array.insert(2, 5)
    array.output()
    print('\n-----')
    array.remove(2)
    array.output()
