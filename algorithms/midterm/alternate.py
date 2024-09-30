def max_alternate(ad_matrix):
    n=len(ad_matrix)
    dp = [[0.0, 0.0] for _ in range(n)]
    for i in range(1,n):
        max_plus = float('-inf')
        max_minus= float('-inf')
        for j in range(n):
            edge_weight = ad_matrix[j][i]
            if edge_weight != float('-inf'):
                if dp[j][0]+edge_weight > max_plus:
                    max_plus = dp[j][0]+edge_weight
                if dp[j][1]-edge_weight > max_minus:
                    max_minus = dp[j][1]-edge_weight
        dp[i][1] = max_plus
        dp[i][0] = max_minus
    return max(dp[n-1][1], dp[n-1][0])
ad_matrix = [[float('-inf'),3,5,float('-inf')],
             [float('-inf'),float('-inf'),7,-2],
             [float('-inf'),float('-inf'),float('-inf'),4],
             [float('-inf'),float('-inf'),float('-inf'),float('-inf')]]

print(max_alternate(ad_matrix))