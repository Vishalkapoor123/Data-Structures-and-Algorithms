class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        return self.display()

    def display(self):
        arr= []
        for i in self.queue:
            arr.append(i)
        return arr
    
    def isEmpty(self):
        if(len(self.queue)==0):
            return True
        return False

    def dequeue(self):
        self.queue.pop(0)
        return self.display()

    
if __name__ == '__main__':
    queue = Queue()
    print(queue.isEmpty())
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.isEmpty())
    print(queue.display())
    print(queue.dequeue())
        
