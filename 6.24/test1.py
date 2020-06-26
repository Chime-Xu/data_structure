class Queue:
    def __init__(self):
        self.entries=[]
        self.length=0
        self.front=0
    def __str__(self):
        printed="<" + str(self.entries)[1:-1] + ">"
        return printed
    def put(self,item):
        self.entries.append(item)
        self.length += 1
    def get(self):
        dequeued=self.entries[self.front]
        self.length -=1
        self.entries=self.entries[1:]
        return dequeued
    def top(self):
        return self.entries[0]
    def size(self):
        return self.length
if __name__ == '__main__':
    q=Queue()
    for i in range(5):
        q.put(i)
    print(q)
    print(q.length)
    print(q.front)
    q.get()
    print(q)
    print(q.top())