# def longestCommonSubsequence(text1,text2):
#     m,n = len(text1),len(text2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     return dp
# print(longestCommonSubsequence('abcd','adc'))
# def lcs(X, Y, m, n):
#     if m == 0 or n == 0:
#         return 0
#     elif X[m-1] == Y[n-1]:
#         return 1 + lcs(X, Y, m-1, n-1)
#     else:
#         return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
# S1 = "AGGTAB"
# S2 = "GXTXAYB"
# print(lcs(S1, S2, len(S1), len(S2)))

# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# Then print the data of node
		print(root.val, end=" "),

		# Now recur on right child
		printInorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Inorder traversal of binary tree is")
	printInorder(root)
