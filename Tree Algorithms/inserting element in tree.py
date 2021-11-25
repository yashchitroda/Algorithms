class Node:

    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """compare the new value with the parent node"""
        if self.data:
            #if data less than root node
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            #if data greater than the root node
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        #If the root is empty
        else:
            self.data = data

        #Print the tree
        def print_tree(self):
            if self.left:
                self.left.print_tree()
            print(self.data)
            if self.right:
                self.right.print_tree()

                def main():
                    #instance for the class Node
                    root = Node(12)
                    #Call the insert function
                    #to insert he elements into the tree
                    root.insert(6)
                    root.insert(11)
                    root.insert(14)
                    root.insert(3)
                    #print he complete tree
                    root.print_tree()
        #Driver code
        if __name__ == "__main__":
            main()
