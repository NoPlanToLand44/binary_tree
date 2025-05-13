class Node:
    def __init__ (self, val): 
        self.val = val
        self.left = None
        self.right = None


#     if root is None:
#         return []
#     values = []
#     stack = [root]
#     # make a while loop to clear all the stack 
#     while stack:
#         current = stack.pop()
#         # append all the values from the stack 
#         values.append(current.val)
#         # stack them LIFO so u can claim them backwards 
#         if current.right is not None: 
#             stack.append(current.right)
#         if current.left is not None:
#             stack.append(current.left)
#     return values 

# print(debth_first_traverse(b))

def depth_first_values(root):
    if root is None: 
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]

print(depth_first_values(a))


