class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():

    def __init__ (self):
        self.root = None


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.left = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
    

    def __delete_node(self, current_node, value):
        #假如要刪除 47左21右22 刪除左21 cyrrent_node = 47 value = 21
        if current_node == None:
            return None
        if value < current_node.value:#current_node = 47 進入遞迴
            #current_node.left = 遞迴 21, 21
            current_node.left = self.__delete_node(current_node.left, value)
            #最後回到這邊current.left = 22右 pop掉21
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            #21.left == None 21.right == 22
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                #current_node = 22右
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node#return 給遞迴

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    
    def min_vlue(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:#pop
            return True
        
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)#return True in there在return 到r_cintains
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)#pop


