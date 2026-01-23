def dfs_post_order(self):
    result = []

#由下到上
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        result.append(current_node.value)#pop掉沒有左右子樹的底放到results
    traverse(self.root)
    return result


#       47
#   21      76
# 18  27  52  82
#
#if 47.left is not None
#21 = current_node
#if 21.left is not None
#18 = current_node
#if 18.left is not None (False)
#if 18.right is not None
#18.append to result pop
#[18]
#if 21.right is not None(True)
#27 = current_node
#if 27.left is not None
#if 27.right is not None
#27.append to result pop
#[18, 27]
#21.left and right is not None(False)
#21.append to result pop
#47.right is not None
#76 = current_node
#76.left is not None
#52 = current_node
#52.left and right is not None
#52.append to result
#[18, 27, 21, 52]
#76.right is not None
#82 = current_node
#82.left and right is not None
#82.append to result pop
#76 = current_node
#76.left and right is not None
#76.append to result
#[18 27 21 52 82 76]
#47.left adn right is not None
#47.append to result
#[18 27 21 52 82 76 47]
#return