class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(data)
        return self.display()
    
    def display(self):
        arr = []
        temp = self.head
        while(temp):
            arr.append(temp.data)
            temp = temp.next
        return arr
    
    def isEmpty(self):
        if(self.head==None):
            return True
        return False
    
    def dequeue(self):
        try:
            temp = self.head.next
            self.head = temp
            return self.display()
        except:
            return "Empty queue"


if __name__ == '__main__':
    queue = Queue()
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.enqueue(3))
    print(queue.display())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue.display())
