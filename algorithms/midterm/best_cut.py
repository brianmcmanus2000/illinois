import numpy as np

def lowest_price(M):
    n = len(M)
    dp = np.zeros([n,n])
    for gap in range(2,n):
        i = 0
        while i+gap < n:
            best_cut = float('inf')
            k=i+1
            if gap == 2:
                dp[i][i+gap] = M[i+gap]-M[i]
            else:
                while k<i+gap:
                    if dp[i][k]+dp[k][i+gap] < best_cut:
                        best_cut = dp[i][k]+dp[k][i+gap]
                    k+=1
                dp[i][i+gap] = best_cut + M[i+gap]-M[i]
            i+=1
    return dp

M = [0,2,3,6,10]
print(lowest_price(M)[0][len(M)-1])