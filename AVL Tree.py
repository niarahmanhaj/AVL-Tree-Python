class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None 

    def height(self,node):
        if not node : 
            return 0
        return node.height

    def get_balance_factor(self,node):
        if not node : 
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self,z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left),self.height(z.right))

        y.height = 1 + max(self.height(y.left),self.height(y.right))
        
        return y 

    def left_rotate(self, z):
        y = z.right 
        T2 = y.left

        y.left = z
        z.right = T2 

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y


    def left_right_rotate(self,z):
        z.left = self.left_rotate(z.left)
        return self.right_rotate(z)

    def right_left_rotate(self,z):
        z.right = self.right_rotate(z.right)
        return self.left_rotate(z)
    
    def rebalance(self,node):
        balance = self.get_balance_factor(node)

        if balance > 1:
            if self.get_balance_factor(node.left) < 0:
                return self.left_right_rotate(node) 
            return self.right_rotate(node)

        if balance < -1:
            if self.get_balance_factor(node.right) > 0:
                return self.right_left_rotate(node)
            return self.left_rotate(node)

        return node

    def insert(self, root, value):
        if not root:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root 
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.rebalance(root)

    def delete(self, root, value):
        if not root:
            return root
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.rebalance(root)
    
    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def print_tree(self, node, level=0):
        if node is not None:
            # Rekursif ke kanan dulu agar posisi kanan ada di atas
            self.print_tree(node.right, level + 1)
            
            # Cetak angka dengan tab/spasi sesuai tingkatan levelnya
            print('        ' * level + '└── ' + str(node.value))
            
            # Rekursif ke kiri agar posisi kiri ada di bawah
            self.print_tree(node.left, level + 1)




tree = AVLTree()
tree.root = tree.insert(tree.root, 10)
tree.root = tree.insert(tree.root, 5)
tree.root = tree.insert(tree.root, 2)
tree.root = tree.insert(tree.root, 4)
tree.root = tree.insert(tree.root, 3)

tree.print_tree(tree.root)