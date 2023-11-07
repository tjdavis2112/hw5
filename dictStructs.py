import random
import time
from collections import defaultdict
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        else:
            return node.value

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append((node.key, node.value))
            self._in_order_traversal(node.right, result)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node


# Function to measure insertion time for a binary tree
def measure_binary_tree_insertion(arr):
    dictionary = BinarySearchTree()
    start_time = time.time()
    for i in arr:
        dictionary.insert(i, i)
    end_time = time.time()
    return end_time - start_time

# Function to measure insertion time for a hash table
def measure_hash_table_insertion(arr):
    d = defaultdict(int)
    start_time = time.time()
    for i in arr:
        d[i] = i
    end_time = time.time()
    return end_time - start_time

n_values = [5, 25, 50, 100, 500, 1000, 2000]  # Adjust this list as needed

binary_tree_times = []
hash_table_times = []


for n in n_values:

    binary_tree_time = 0
    hash_table_time = 0
    arr = [random.randint(1, 1000) for _ in range(n)]

    for _ in range(1000):
        binary_tree_time += measure_binary_tree_insertion(arr.copy())
        hash_table_time += measure_hash_table_insertion(arr.copy())
        print(binary_tree_time)
    
    binary_tree_times.append(binary_tree_time)
    hash_table_times.append(hash_table_time)

plt.plot(n_values, binary_tree_times, marker='o', label='Binary Tree')
plt.plot(n_values, hash_table_times, marker='x', label='Hash Table')
plt.xlabel('n (Number of Insertions)')
plt.ylabel('Time (s)')
plt.title('Insertion Time for Binary Tree vs Hash Table')
plt.legend()
plt.grid(True)
plt.show()