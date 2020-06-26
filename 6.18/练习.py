class Array:
    def __init__(self, capacity):  #特殊
        self.array = [None] * capacity  # 空数组
        self.size = 0  # 数组有效元素个数

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        if self.size >= len(self.array):  # 数组长度
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            # 插入指定的位数,指定下标的元素往后去一位,倒序插入,range前闭后开
            self.array[i + 1] = self.array[i]
        self.array[index] = element  # 顺序插入元素
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        for i in range(index, self.size, 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def addcapacity(self):
        # capacity 这边不存在   self.size可用
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
    array.remove(2)
    array.output()
    print('\n')
    array.remove(2)
    array.output()