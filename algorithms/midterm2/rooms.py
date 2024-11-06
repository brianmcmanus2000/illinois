def find_rooms(S):
    dp = [[0 for x in range(3)] for y in range(len(S)+1)] 
    for n in range(len(S)):
        dp[n+1][0] = max(dp[n][0],dp[n][1],dp[n][2])
        dp[n+1][1] = dp[n][0]+S[n]
        dp[n+1][2] = dp[n][1]+S[n]
    return max(dp[n+1][0],dp[n+1][1],dp[n+1][2])
S = [10,11,12,13,21,5,8,9,10]
val = find_rooms(S)
print(val)