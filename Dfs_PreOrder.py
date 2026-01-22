def dfs_pre_order(self):
    result = []


#由上而下由左至右


    def traverse(current_node):
        #把node放進result
        #如果到最低節點左右下方都沒有結點就會pop掉
        #持續recursion
        result.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return result