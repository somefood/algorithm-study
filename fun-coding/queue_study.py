class MyQueue(list):
    def queue(self,data):
        self.append(data)
    def dequeue(self):
        data = self[-1]
        del self[-1]
        return data


queue_list = MyQueue()
for index in range(10):
    queue_list.queue(index)

print(queue_list)

while queue_list:
    print(queue_list.dequeue())
