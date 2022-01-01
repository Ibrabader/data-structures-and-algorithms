from python.code_challenges.trees.trees import binary_search_tree


class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if data== self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left= BinarySearchTree(data)
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BinarySearchTree(data)
        
    def search(self,value):
        if value == self.data:
            return True
        if value < self.data:
            if self.left:
               return self.left.search(value)
            else:
                return False
        if value > self.data :
            if self.right:
                return self.right.search(value)
                
            else:
                return False
            
    def in_order_traversal(self):
        elements =[]
        
        if self.left:
            elements+=self.left.in_order_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements+=self.right.in_order_traversal()
        
        return elements
    
    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def calculate_sum(self):
        sum=0
        leftV=0
        rightV=0
        if self.left:
           leftV= self.left.calculate_sum()
        if self.right:
            rightV=self.right.calculate_sum()
        sum= self.data+leftV+rightV
        return sum
    
    def delete(self,value):
        if value< self.data:
            if self.left:
                self.left = self.left.delete(value)
            if self.right:
                self.right = self.right.delete(value)
            else:
                if self.left and self.right is None :
                    return None 
                elif self.left is None :
                    return self.right 
                elif self.right is None :
                    return self.right 
                        
                min_value= self.right.find_min()
                self.data = min_value 
                

    
    def minDiffInBST(self, root) :
        stack = []
        curr = root
        prev = None
        minimum = float('inf')
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev:
                    minimum = min(minimum, curr.val - prev.val)
                prev = curr
                curr = curr.right
        return minimum
    
    def binaryTreePaths(self, root):
            def dfs(root, output = ''):
                if not root:
                    return "empty list"
                if not root.left and not root.right:
                    tmp.append(str(root.val))
                    res.append("->".join(tmp))
                    tmp.pop()
                    return
                tmp.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
                tmp.pop()
            tmp = []
            res = []
            dfs(root)
            return res
        
    def isSymmetric(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            return self.isMirror(root,root)

        def isMirror(self,leftroot,rightroot):
            if leftroot and rightroot :
                return leftroot.val == rightroot.val and self.isMirror(leftroot.left,rightroot.right) and self.isMirror(leftroot.right,rightroot.left)
            return leftroot == rightroot

    def isSameTree(self, p, q) :
        # we are passing the root not the tree as whole 
        # p=p.root,q=q.root
        if not p and not q :
            return True
        if not p or not q :
            return False
        if  p.val != q.val :
            return False
        # if it a function we should not put self
        if (  self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)  ):
              return True
            
        else:
            return False


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
        
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18,'5', 34]

    numbers = [15,12 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    # print("In order traversal:", numbers_tree.in_order_traversal())
    # print("Pre order traversal:", numbers_tree.pre_order_traversal())
    # print("Post order traversal:", numbers_tree.post_order_traversal())

            