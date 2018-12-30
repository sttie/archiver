class BinaryTree:
    def __init__(self, key=None, value=None):
        self.root = TreeNode(key, value)
        self.size = 1 if value else 0
    
    def put(self, value, key=0):
        if self.root.key:
            # return
            self._put(key, value, self.root)
        else:
            self.root.key = key
            self.root.value = value
            # return
            self.root
        
        self.size += 1
    
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_сhild():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                # return current_node.left_child
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                # return current_node.right_child
        
    def __len__(self):
        return self.size
    

class TreeNode:
    # key - приоритет, value - значение
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
    
    def has_left_сhild(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def print_everything(self):
        pass
    
    def __iter__(self):
        yield self.left_child, self.right_child

if __name__ == "__main__":
    a = BinaryTree()
    a.put("a", 134)
    a.put("b", 1)
    a.put("c", 141414)
    print(a.root.key)
    print("\n\n")
    print(a.root.left_child.key)
    print(a.root.left_child.value)
    print("\n\n")
    print(a.root.right_child.key)
    print(a.root.right_child.value)