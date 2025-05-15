import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from recursion import Node


@pytest.fixture
def single_node_tree():
    return Node(10)

@pytest.fixture
def populated_tree():
    root = Node(10)
    for val in [5,15,3,7,12,17]:
        root.insert(val)
    return root

def test_inorder_traversal(populated_tree):
    assert populated_tree.inOrder(populated_tree) == [3,5,7,10,12,15,17]

def test_preorder_traversal(populated_tree):
    assert populated_tree.preOrder(populated_tree) == [10,5,3,7,15,12,17]

@pytest.mark.parametrize("values, expected", [
    ([10, 5, 15],       [5, 10, 15]),
    ([20, 10, 30, 25],  [10, 20, 25, 30]),
    ([1],               [1]),
])

def test_inorder_parametrized(values, expected):

    root = Node(values[0])
    for v in values[1:]:
        root.insert(v)
   
    result = root.inOrder(root)

    assert result == expected
