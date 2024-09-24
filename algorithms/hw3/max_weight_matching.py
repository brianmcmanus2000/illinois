# Implementation of the maximum weight matching algorithm for a tree

from collections import defaultdict

def max_weight_matching(tree, weights, root):
    n = len(tree)
    dp = [[0, 0] for _ in range(n)]
    
    def dfs(u):
        for v in tree[u]:
            dfs(v)
        dp[u][0] = sum(max(dp[v][0], dp[v][1]) for v in tree[u])
        for v in tree[u]:
            dp[u][1] = max(dp[u][1], dp[v][0] + weights[u][v] + sum(dp[w][1] for w in tree[u] if w != v))
    dfs(root)
    return max(dp[root][0], dp[root][1])

tree = defaultdict(list)

tree[0] = [1, 2, 3]

tree[1] = [4, 5]

tree[2] = []

tree[3] = [6, 7]

tree[4] = [8, 9]

tree[5] = [10]

tree[6] = []

tree[7] = [11, 12, 13]

tree[8] = []

tree[9] = []

tree[10] = [14, 15]

tree[11] = [16]

tree[12] = []

tree[13] = []

tree[14] = []

tree[15] = []

tree[16] = []



# Weights of the edges

weights = defaultdict(lambda: defaultdict(int))

weights[0][1] = 5

weights[1][0] = 5

weights[0][2] = 9

weights[2][0] = 9

weights[0][3] = -2

weights[3][0] = -2

weights[1][4] = -3

weights[4][1] = -3

weights[1][5] = 6

weights[5][1] = 6

weights[4][8] = -6

weights[8][4] = -6

weights[4][9] = -2

weights[9][4] = -2

weights[5][10] = 2

weights[10][5] = 2

weights[3][6] = 1

weights[6][3] = 1

weights[3][7] = 3

weights[7][3] = 3

weights[7][11] = 7

weights[11][7] = 7

weights[7][12] = 4

weights[12][7] = 4

weights[7][13] = 2

weights[13][7] = 2

weights[10][14] = -3

weights[14][10] = -3

weights[10][15] = 4

weights[15][10] = 4

weights[11][16] = 6

weights[16][11] = 6

# Run the algorithm on this example tree starting from root 0
max_matching_weight = max_weight_matching(tree, weights, 0)
print(max_matching_weight)
