def coinChange(coins: list[int], amount: int) -> int:
    # dp[i] := the minimum number Of coins to make up i
    dp = [0] + [amount + 1] * amount

    for coin in coins:
      for i in range(coin, amount + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == amount + 1 else dp[amount]
def make_changes(N, K, target, coins):
    dp = [[False for _ in range(K + 1)] for _ in range(target + 1)]
    dp[0][0] = True

    for i in range(1, target + 1):
        for j in range(K + 1):
            for coin in coins:
                if coin <= i and j > 0 and dp[i - coin][j - 1]:
                    dp[i][j] = True
                    break

    # Return the result
    return dp[target][K]

N = 5
K = 3
target = 11
coins = [1, 10, 5, 8, 6]

# Function call
result = make_changes(N, K, target, coins)
if result:
    print('1')
else:
    print('0')

c1 = [1,5,10,25]
a1 = 30
print(coinChange(c1,a1))