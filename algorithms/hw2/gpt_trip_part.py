def subsetSum(S, n, a, b, c, lookup, partition):
    # Base case: if all subsets are filled
    if a == 0 and b == 0 and c == 0:
        return True
    # Return False if no items left
    if n < 0:
        return False
    # Construct a key for memoization
    key = (a, b, c, n)
    
    if key not in lookup:
        A = False
        B = False
        C = False
        
        # Try including S[n] in subset A
        if a - S[n] >= 0:
            partition[0].append(S[n])
            A = subsetSum(S, n - 1, a - S[n], b, c, lookup, partition)
            if not A:  # Backtrack if A is not valid
                partition[0].pop()

        # Try including S[n] in subset B
        if not A and (b - S[n] >= 0):
            partition[1].append(S[n])
            B = subsetSum(S, n - 1, a, b - S[n], c, lookup, partition)
            if not B:  # Backtrack if B is not valid
                partition[1].pop()

        # Try including S[n] in subset C
        if (not A and not B) and (c - S[n] >= 0):
            partition[2].append(S[n])
            C = subsetSum(S, n - 1, a, b, c - S[n], lookup, partition)
            if not C:  # Backtrack if C is not valid
                partition[2].pop()

        lookup[key] = A or B or C

    return lookup[key]

def partition(S):
    if len(S) < 3:
        return False
    lookup = {}
    total = sum(S)
    if (total % 3) != 0:
        return False

    # Partition to store the three subsets
    partition = ([], [], [])
    if subsetSum(S, len(S) - 1, total // 3, total // 3, total // 3, lookup, partition):
        print("Set can be partitioned into three subsets with equal sum:")
        print("Subset 1:", partition[0])
        print("Subset 2:", partition[1])
        print("Subset 3:", partition[2])
        return True
    else:
        print("Set cannot be partitioned into three subsets with equal sum.")
        return False


# Example usage
S = [7, 3, 2, 1, 5, 4, 9]
partition(S)
