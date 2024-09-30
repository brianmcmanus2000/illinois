import numpy as np

def best_parens(array):
    n = len(array)
    dp = np.zeros([n,n])
    i = n-1
    while i >= 0:
        k=0
        while k < n:
            j=i
            if i == k:
                dp[i][k] = array[i]
            else:
                value = float('inf')
                while j<k:
                    test = (dp[i][j]+dp[j+1][k])/2
                    if test < value:
                        value = test
                    j+=1
                dp[i][k] = value
            print(dp[i][k])
            k+=1
        i-=1
    print(dp)
    print(dp[0][n-1])
array = [8, 6, 7, 5, 3, 0, 9]
best_parens(array)