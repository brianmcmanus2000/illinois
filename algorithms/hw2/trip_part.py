def subsetSum(S,n,a,b,c,lookup):
    if a== 0 and b==0 and c==0:
        return True
    if n<0:
        return False
    key = (a,b,c,n)
    if key not in lookup:
        A = False
        B = False
        C = False
        if a - S[n] >=0:
            A = subsetSum(S, n - 1, a - S[n], b, c, lookup)
        if not A and (b - S[n] >= 0):
            B = subsetSum(S, n-1, a, b-S[n], c, lookup)
        if (not A and not B) and (c - S[n] >= 0):
            C = subsetSum(S, n-1, a, b, c-S[n], lookup)
        lookup[key] = A or B or C
        #print(lookup)
    return lookup[key]

def partition(S):
    if len(S) < 3:
        return False
    lookup = {}
    total = sum(S)
    return (total %3) == 0 and subsetSum(S,len(S)-1,total//3,total//3,total//3,lookup)
    

S = [7, 3, 2, 1, 5, 4, 10]
if partition(S):
    print("set can be partitioned")
else:
    print("set cannot be partitioned")