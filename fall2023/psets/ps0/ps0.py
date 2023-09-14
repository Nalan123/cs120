#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    if v is None: 
        return 0
    
    left_subtreee_size = calculate_sizes(v.left)

    right_subtree_size = calculate_sizes(v.right)

    total_size  = left_subtreee_size + right_subtree_size + 1

    v.size = total_size

    return total_size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h
def find_vertex(r): 
    # Your code goes here
    if not r:
        return None
    
    def find_size(v):
        if not v:
            return None 


        vertex = None 

        if largest_subtree(v, r) <= r.size/2:
            vertex = v 
        elif v.left and largest_subtree(v.left, r) > r.size/2:
            return find_size(v.left)
        else:
            return find_size(v.right)

        return vertex

    def largest_subtree(v,r):
        max_size = float("-inf")
        if v.left and not v.right:
            max_size = max(v.left.size, r.size- v.size)
        elif v.right and not v.left: 
            max_size = max(v.right.size, r.size- v.size)
        else:
            max_size = r.size - v.size

        return max_size

    return find_size(r)


