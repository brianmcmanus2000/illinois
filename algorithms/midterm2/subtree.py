class Node:
   def __init__(self, data, left, right, isLeaf:bool):
      self.left = left
      self.right = right
      self.isLeaf = isLeaf
      self.data = data

def find_largest_subtree(root: Node, dp):
    if root == None:
        return 0
    print("node = "+str(root.data))
    if root.isLeaf:
       dp[root.data-1]=0
       print("found a leaf")
       return
    right = find_largest_subtree(root.right,dp)
    left = find_largest_subtree(root.left,dp)
    if (right == None) or (left == None):
       print("Missing child")
       dp[root.data-1] = 0
       return 0
    else:
        dp[root.data-1] = 1+min(dp[right.data-1],dp[left.data-1])
    
node7  = Node(7,None,None,True)
node10 = Node(10,None,None,True)
node11 = Node(11,None,None,True)
node13 = Node(13,None,None,True)
node14 = Node(14,None,None,True)
node15 = Node(15,None,None,True)
node16 = Node(16,None,None,True)
node17 = Node(17,None,None,True)
node18 = Node(18,None,None,True)
node8  = Node(8,node13,node14,False)
node9  = Node(9,node15,node16,False)
node12 = Node(12,node17,node18,False)
node4  = Node(4,node7,node8,False)
node5  = Node(5,node9,node10,False)
node6  = Node(6,node11,node12,False)
node2  = Node(2,node4,node5,False)
node3  = Node(3,node6,None,False)
node1  = Node(1,node2,node3,False)

dp = [0]*18
find_largest_subtree(node1,dp)
print(dp)