import numpy as np
from numpy import unravel_index

def longest_increasing_subsequence_with_icky(A, Icky, k):
    n = len(A)
    
    # DP table, dp[i][j] represents the LIS ending at A[i] with exactly j icky numbers
    dp = np.full((n,k+1),-1000)
    for i in range(n):
        if Icky[i]==True:
            dp[i][1]=1
        else:
            dp[i][0]=1
    for i in range(n):
        for j in range(k + 1):
            # For each A[i], look at previous A[t] where A[t] < A[i]
            for t in range(i):
                if A[t] < A[i]:
                    # If A[i] is not icky, it can extend the subsequences with j icky numbers
                    if Icky[i] == False:
                        dp[i][j] = max(dp[i][j], dp[t][j] + 1)
                    # If A[i] is icky, it can only extend subsequences with j-1 icky numbers
                    elif Icky[i] == True and j > 0:
                        dp[i][j] = max(dp[i][j], dp[t][j - 1] + 1)
    
    # Find the maximum length of LIS with at most k icky numbers
    max_index = unravel_index(dp.argmax(), dp.shape)
    return max_index, dp

A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
Icky = [True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True]
k=2
max_index, dp = longest_increasing_subsequence_with_icky(A,Icky,k)
print(f"The longest subsequence with at most {k} icky numbers ends at {A[max_index[0]]} at index {max_index[0]} and has length {dp[max_index]}")