def can_partition_disjoint_subsequences(P, T):
    k = len(P)
    n = len(T)
    
    # Step 1: Build DP1 - Forward DP to match prefix of P
    DP1 = [[False] * (k + 1) for _ in range(n + 1)]
    DP1[0][0] = True  # Empty pattern can match with empty text
    
    for i in range(1, n + 1):
        DP1[i][0] = True  # Empty pattern matches with any text prefix
        for j in range(1, k + 1):
            DP1[i][j] = DP1[i - 1][j]  # Skip T[i-1]
            if T[i - 1] == P[j - 1]:
                DP1[i][j] = DP1[i][j] or DP1[i - 1][j - 1]  # Use T[i-1] to match P[j-1]
    
    # Step 2: Build DP2 - Backward DP to match suffix of P
    DP2 = [[False] * (k + 1) for _ in range(n + 1)]
    DP2[n][0] = True  # Empty pattern can match with empty text
    
    for i in range(n - 1, -1, -1):
        DP2[i][0] = True  # Empty pattern matches with any text suffix
        for j in range(1, k + 1):
            DP2[i][j] = DP2[i + 1][j]  # Skip T[i]
            if T[i] == P[k - j]:  # Match with reverse of P
                DP2[i][j] = DP2[i][j] or DP2[i + 1][j - 1]  # Use T[i] to match P[k-j]
    
    # Step 3: Check for disjoint subsequences
    for i in range(n):
        for j in range(k):
            if DP1[i][j] and DP2[i + 1][k - j]:
                return True
    
    return False


# Test cases
P1 = "PPAP"
T1 = "PENPINEAPPLEAPPLEPEN"

P2 = "PEEPLE"
T2 = "PENPINEAPPLEAPPLEPEN"

P3 = "PIKOTARO"
T3 = "PENPINEAPPLEAPPLEPEN"

results = {
    "Test 1 (PPAP in PENPINEAPPLEAPPLEPEN)": can_partition_disjoint_subsequences(P1, T1),
    "Test 2 (PEEPLE in PENPINEAPPLEAPPLEPEN)": can_partition_disjoint_subsequences(P2, T2),
    "Test 3 (PIKOTARO in PENPINEAPPLEAPPLEPEN)": can_partition_disjoint_subsequences(P3, T3)
}

print(results)
