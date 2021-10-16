class Node:
    def __init__(self, data):
        self.root = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if(self.head==None):
            self.head = Node(data)
        else:
            newNode = Node(data)
            self.head.next = newNode
        return self.head.root

    def isEmpty(self):
        if(self.head==None):
            return True
        return False
    
    def display(self):
        arr = []
        temp = self.head
        while(temp):
            arr.append(temp.root)
            temp = temp.next
        return arr

    def pop(self):
        temp  = self.head
        prevNode = None
        while(temp.next):
            prevNode = temp
            temp = temp.next
        prevNode.next = None
        return self.display()
    
if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    print(stack.push(1))
    print(stack.push(2))
    print(stack.isEmpty())
    print(stack.display())
    print(stack.pop())

    
