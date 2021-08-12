#!/usr/bin/env python3
from __future__ import annotations
from typing import Optional
from random import choices


class TreeNode:
    def __init__(self, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None, value: str = ""):
        self._left = left
        self._right = right
        self._value = value
        self._count = 1

    @property
    def left_node(self) -> Optional[TreeNode]:
        return self._left

    @left_node.setter
    def left_node(self, left: Optional[TreeNode]):
        self._left = left

    @property
    def right_node(self) -> Optional[TreeNode]:
        return self._right

    @right_node.setter
    def right_node(self, right: Optional[TreeNode]):
        self._right = right

    @property
    def node_value(self):
        return self._value

    @node_value.setter
    def node_value(self, value: str):
        self._value = value

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int):
        self._count += value

    def __repr__(self):
        return (
            f'{{"value": "{self.node_value}", "count": {self.count}, "left": {self.left_node}, "right": {self.right_node}}}'
        )


class Tree:
    def __init__(self):
        self._root: TreeNode = TreeNode(value="")

    def insert_value(self, value: str, start: Optional[TreeNode] = None) -> TreeNode:

        if not start:
            start = self._root

        insertedNode: TreeNode = TreeNode(value=value)

        # if we're on a new root, set its value
        if not start.node_value:
            start.node_value = value
            start.count += 1
            return start

        if value < start.node_value:
            if start.left_node:
                insertedNode = self.insert_value(value, start.left_node)
            else:
                start.left_node = insertedNode

        elif value > start.node_value:
            if start.right_node:
                insertedNode = self.insert_value(value, start.right_node)
            else:
                start.right_node = insertedNode
        else:
            start.count += 1

        return insertedNode

    def find_value(self, value: str, start: TreeNode) -> TreeNode:
        if start.node_value == value:
            return start

        if value < start.node_value:
            assert start.left_node is not None
            return self.find_value(value, start.left_node)
        else:
            assert start.right_node is not None
            return self.find_value(value, start.right_node)

    def dfs(self, start: TreeNode) -> str:

        output = f"{start.node_value}"
        if start.left_node:
            output = self.dfs(start.left_node) + output

        if start.right_node:
            output += self.dfs(start.right_node)

        return output

    def __repr__(self):
        return f"{self._root}"


def main():
    tree = Tree()

    letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    for letter in choices(letters, k=100):
        tree.insert_value(letter)

    print(tree)
    print(tree.dfs(tree._root))


if __name__ == "__main__":
    main()
