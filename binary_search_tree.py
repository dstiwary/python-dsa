class Node :
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

# TODO: Add Multiple parameters in constructor and in add node method 
# TODO: Figure out why remove is not working 
class Tree:
    root = None 
    level = 0
    
    # ^~ Data Abstraction Wrapper, so that clients do not have to pass the root or assign back to the root 
    def add_node(self, *values):
        for value in values:
            self.root = self.__add_node(self.root, value)
    
    def __add_node(self, node, value):
        if node is None:
            return Node(value)
        
        if value > node.value:
            # Add to right 
            node.right = self.__add_node(node.right, value)
        else:
            # Add to left 
            node.left = self.__add_node(node.left, value)
            
        return node 
    
    # ^~ Data Abstraction Wrapper, so that clients do not have to pass the root or assign back to the root
    def print_sorted(self):
        self.__print_sorted(self.root)

    def __print_sorted(self, node):
        if node is not None:
            self.__print_sorted(node.left)
            print(node.value)
            self.__print_sorted(node.right)
    
    # ^~ Data Abstraction Wrapper, so that clients do not have to pass the root or assign back to the root
    def print_reverse_sorted(self):
        self.__print_reverse_sorted(self.root)
    
    def __print_reverse_sorted(self, node):
        if node is not None:
            self.__print_reverse_sorted(node.right)
            print(node.value)
            self.__print_reverse_sorted(node.left)
            
    def print_tree(self):
        self.__print_tree(self.root)
    
    def __print_tree(self, node):
        if node is None:
            return
        self.level += 1
        self.__print_tree(node.right)
        print(" " * self.level * 4, node.value)
        self.__print_tree(node.left)
        self.level -= 1
    
    def remove(self, *values):
        for value in values:
            self.root = self.__remove(self.root, value)
    
    def __remove(self, node, value):
        # ~* If the node is none in that case we cannot find the value in that case remove
        if node is None: 
            return None
        
        # ~* HUNT for the value
        if value > node.value:
            # * Then continue searching on right 
            node.right = self.__remove(node.right, value)
        elif value < node.value : 
            # * Then continue searching on left 
            node.left = self.__remove(node.left, value)
        else: 
            # ~* FOUND IT !!! 
            
            # ^ Use or as a condition in Coalesce Operator 
            if node.left is None or node.right is None:
                return node.left or node.right 
            
            # # * If the node does not have a left and right dependency then return None
            # if node.right is None and node.left is None: 
            #     return None 
            # # * If the node does not have a left dependency then return the right node --> Girl Child
            # elif node.right is not None and node.left is None: 
            #     return node.right
            # # * If the node on left has a dependency then return the left node --> Boy Child
            # elif node.left is not None and node.right is None: 
            #     return node.left 
            # # * If the node has both the child
            else: 
                # ^ Move to the right 
                successor = node.right
                # ^ Find the left most value of the immediate right value  
                while successor.left is not None:
                    successor = successor.left 
                node.value = successor.value
                
                # * Kill the successor node which is go the right of the node 
                node.right = self.__remove(node.right, successor.value)
                
        # ~* Always remember to return the node no matter what
        return node
            
        
    
ped = Tree()
ped.add_node(5, 7, 9, 10, 1 , 4, 8, 6, 2,)
ped.add_node(3)
ped.print_tree()
ped.remove(5, 9)
print("After deletion of the node.")
ped.print_tree()

# ped.print_sorted()
# print("Reverse Sorted")
# ped.print_reverse_sorted()

            
            
        
        
            

    
        
        