def depth_first_values(root):
    if root is None: 
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val] + left_values + right_values