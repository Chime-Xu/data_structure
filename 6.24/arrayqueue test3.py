# 队列  先进先出
class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front=0

    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def put(self, item):  # 入队 enquene
        self.entries.append(item)
        self.length += 1

    def get(self):  # 可加个判断是否为空
        dequeued = self.entries[self.front]
        self.length = self.length - 1
        self.entries = self.entries[1:]
        return dequeued

    def top(self):
        return self.entries[0]

    def size(self):
        return self.length

if __name__ == '__main__':
    q = Queue()
    for i in range(1, 5):
        q.put(i)
    print(q)
    print(q.get())
    print(q)
    print(q.size())
    print(q.top())
