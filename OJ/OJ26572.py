# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:31:56 2024

@author: Lenovo
"""

import re
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(node):
    if isinstance(node, str):
        return node
    if node.value == '*':
        left = dfs(node.left)
        right = dfs(node.right)
        if isinstance(node.left, Node) and node.left.value == '+':
            left = f'({left})'
        if isinstance(node.right, Node) and node.right.value == '+':
            right = f'({right})'
        return left + '*' + right
    else:
        return dfs(node.left) + node.value + dfs(node.right)

def helper(tokens):
    stack = []
    for token in tokens:
        if token == ')':
            sub_expr = []
            while stack and stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()
            stack.append(build_tree(sub_expr[::-1]))
        else:
            stack.append(token)
    return stack

def build_tree(tokens):
    tokens = helper(tokens)
    while '*' in tokens:
        index = tokens.index('*')
        node = Node('*', tokens[index - 1], tokens[index + 1])
        tokens = tokens[:index - 1] + [node] + tokens[index + 2:]
    if len(tokens) == 1:
        return tokens[0]
    left_operand = tokens[0]
    for i in range(1, len(tokens), 2):
        left_operand = Node(tokens[i], left_operand, tokens[i + 1])
    return left_operand

while True:
    try:
        expression = input()
        tokens = [token for token in re.split(r"(\D)", expression) if token]
        root = build_tree(tokens)
        print(dfs(root))
    except EOFError:
        break