class Stack:

    def __init__(self):
        self.stack=[]

    def push(self,element):
        self.stack.append(element)

    def display(self):
        for i in self.stack:
            print(i, end=" ")
    
    def isEmpty(self):
        if(len(self.stack)==0):
            return True
        return False

if __name__ == '__main__':
    a = Stack()
    print(a.isEmpty())
    a.display()
    a.push(1)
    a.push(2)
    a.display()
    print(a.isEmpty())
    
