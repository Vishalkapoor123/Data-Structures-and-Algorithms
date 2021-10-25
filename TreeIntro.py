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
            return newNode
        if(data < root.data):
            root.left = self.insert(root.left, data)
        elif(data > root.data):
            root.right = self.insert(root.right, data)
        elif(data == root.data):
            return  root
        return root
            
    #Cliennt facing method
    def insert_client(self, data):
        temp = self.root
        self.root = self.insert(temp,data)

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

    def min(self, root):
        if(root.left==None): return root
        elif(root.left):
            return self.min(root.left)

    def min_client(self):
        temp=self.root
        return self.min(temp)

    def deleteMin(self,root):
        if(root.left==None):
            return root.right
        root.left = self.deleteMin(root.left)
        return root

    #Internal delete method i.e. not client facing
    def delete(self, root, data):
        if(root == None): return None
        if(root.data<data):
            root.left = self.delete(root.left , data)
        elif(root.data > data):
            root.right = self.delete(root.right, data)
        else:
            temp = root
            root = self.min(temp.right)
            root.right = self.deleteMin(temp.right)
            root.left = temp.left
        return root
            
    #Cliennt facing delete method
    def delete_client(self, data):
        temp = self.root
        self.root = self.delete(temp,data)

    def test(self):
        print(self.root.left.data)
        print(self.root.left.left.data)
    
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
    tree.insert_client(3)
    tree.insert_client(7)
    tree.insert_client(0)
    tree.insert_client(11)
    tree.inorder_client() 
    # tree.test() 
    print(tree.search(1))
    tree.delete_client(5)
    print("minimum {}".format(tree.min_client().data))
    tree.inorder_client()  


