# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Hannah
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)


print()

print(len(lbt))
print(lbt.height(lbt.root()))
print()


# Performing a preorder traverse on our binary tree
print("Here is the preorder traverse")
print()
lbt.preorder_traverse(lbt.root())
print()
# Performing a postorder traverse on our binary tree
print("Here is the postorder traverse")
print()
lbt.postorder_traverse(lbt.root())
print()
# Performing an inorder traverse on our binary tree
print("Here is the inorder traverse")
print()
lbt.inorder_traverse(lbt.root())
