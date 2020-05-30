class NodePatient:
    def __init__(self, patient):
        self.patient = patient
        self.key = patient.patient_id
        self.left = None
        self.right = None
        self.height = 1

class NodePatientRankValue:
    def __init__(self, patient):
        self.patient = patient
        self.key = patient.rankValue
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def __init__(self):
        self.root = None

    # SEARCH for patient using id
    def search(self, key):
        node = self.search_recur(self.root, key)

        if node is not None:
            return node.patient
        else:
            return "Patient with name " + key + " does not exist in the database."

    # INSERT an object
    def insert(self, node_obj):
        # self.root = self.insert_recur(self.root, NodePatient(obj))
        self.root = self.insert_recur(self.root, node_obj)

    # IN-ORDER traversal: (left -> root -> right) (Ascending order of patient id)
    def in_order(self):
        self.in_order_recur(self.root)

    # Recursive method to search for id
    def search_recur(self, curr_root, key):
        # Case 1: if root is None, or id is at root
        if (curr_root is None) or (curr_root.key == key):
            return curr_root
        # Case 2: if id is greater than root's id
        if key > curr_root.key:
            return self.search_recur(curr_root.right, key)
        # Case 3: if id is smaller than root's id
        return self.search_recur(curr_root.left, key)

    # Recursive method to insert a node and balance the tree
    def insert_recur(self, curr_root, node):
        # insert in the right position
        if curr_root is None:
            return node
        elif node.key > curr_root.key:  # if value to be insert larger than value at root node, go right
            curr_root.right = self.insert_recur(curr_root.right, node)
        else:  # if value to be insert smaller than value at root node, go left
            curr_root.left = self.insert_recur(curr_root.left, node)

        # Update height of root node
        self.update_height(curr_root)

        # get the height difference
        diff = self.get_difference(curr_root)

        # Perform Rotation to balance the tree
        # There are 4 cases:
        # Case 1: Left left -> rotate right
        if (curr_root.left is not None) and (node.key < curr_root.left.key) and (diff > 1):
            return self.right_rotate(curr_root)

        # Case 2: Right Right -> rotate left
        if (curr_root.right is not None) and (node.key > curr_root.right.key) and (diff < -1):
            return self.left_rotate(curr_root)

        # Case 3: Left Right -> rotate left, then rotate right
        if (curr_root.left is not None) and (node.key > curr_root.left.key) and (diff > 1):
            curr_root.left = self.left_rotate(curr_root.left)
            return self.right_rotate(curr_root)

        # Case 4: Right Left -> rotate right, then rotate left
        if (curr_root.right is not None) and (node.key < curr_root.right.key) and (diff < -1):
            curr_root.right = self.right_rotate(curr_root.right)
            return self.left_rotate(curr_root)

        return curr_root

    # Recursive method to in-order traverse the tree (left -> root -> right) (Ascending order of object's key)
    def in_order_recur(self, node):
        if node is None:
            return

        self.in_order_recur(node.left)
        print(node.patient, end="\n")
        self.in_order_recur(node.right)

    # Left Rotation around a node
    def left_rotate(self, node):
        R = node.right  # right branch of the node

        # rotation
        node.right = R.left  # right of node is now left of R :
        R.left = node  # left of R now points to node:

        # update height of nodes
        self.update_height(node)
        self.update_height(R)

        return R

    # Right Rotation around a node
    def right_rotate(self, node):
        L = node.left  # left branch of node

        # rotation
        node.left = L.right  # left of node is now right of 'L' : N.left = B3
        L.right = node  # right of 'L' now points to node: L.right = N

        # update height of nodes:
        self.update_height(node)
        self.update_height(L)

        return L

    # return height of a node
    def get_height(self, node):
        return node.height if (node is not None) else 0

    # Update height of a node
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # returns height different of left and right branch of a mode
    def get_difference(self, node):
        return (self.get_height(node.left) - self.get_height(node.right)) if (node is not None) else 0

