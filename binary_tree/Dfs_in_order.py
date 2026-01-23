#按順序
def des_in_order(self):
    result = []

    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        result.append(current_node.value)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return result

#   47
#  21 76
#18 27 52 82

#47.left is not None
#current = 21
#21.left is not None
#current = 18
#18.left is not None False
#18.append to result
#[18]
#18.right is not None
#[18 21]
#21.right is not None
#current = 27
#27.left is not None:
#27.append to result
#[18 21 27]
#27.right is not None
#47.appedn to result
#[18 21 27 47]
#47.right is not None
#76.left is not None
# current =52
#52.left is not None
#51.appedn to result
#76.append to result
#[18 21 27 47 52 76]
#76.right is not None
#82 = current
#82.left is not None
#82.append to result
#[18 21 27 47 52 76 82]
#return