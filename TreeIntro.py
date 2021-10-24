class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    #Internal insert methpd i.e. not client facing
    def insert(self, root, data):
        newNode = Node(data)
        if(root == None):
            root = newNode
        if(data < root.data):
            root.left = self.insert(root.left, data)
        elif(data > root.data):
            root.right = self.insert(root.right, data)
        elif(data == root.data):
            return  root
        return newNode
            
    #Cliennt facing method
    def insert_client(self, data):
        temp = self.root
        self.insert(temp,data)

    def search(self, data):
        temp = self.root
        while(temp):
            if(temp.data == data):
                return True
            elif(temp.data > data):
                temp = temp.left
            elif(temp.data < data):
                temp = temp.right
        if(temp == None):
            return False


    #Internal method
    def inorder(self, root):
        if(root.left):
            self.inorder(root.left)
        print(root.data)
        if(root.right):
            self.inorder(root.right)
            
    #Client facing inorder method
    def inorder_client(self):
        self.inorder(self.root)



################################Starter code ################################
       

if __name__ == '__main__':
    tree = BinaryTree(5)
    tree.insert_client(1)
    tree.insert_client(10)
    tree.inorder_client()  


