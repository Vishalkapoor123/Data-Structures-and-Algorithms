class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = Node(data)

    def display(self):
        print("##############  Displaying Linked List #############")
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def delete(self,data):
        temp = self.head
        if(data == self.head.data):
            self.head = self.head.next
        while(temp.next):
            if(temp.next.data==data):
                temp.next = temp.next.next
            else:
                temp = temp.next

    def isEmpty(self):
        if(self.head==None):
            return True
        else:
            return False



############################Starter Code ############
if __name__ == '__main__':
    ll = LinkedList(1)
    ll.display()
    ll.insert(2)
    ll.insert(7)
    ll.display()
    ll.delete(7)
    ll.display()
    