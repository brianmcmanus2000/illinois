import numpy as np
A = [8,2,3,5]
B = [1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1]

C = np.convolve(A,B)
distinct_sums = set()
for sum in C:
    if sum != 0:
        distinct_sums.add(sum)
print(C)
print(len(distinct_sums))
#print("Number of distinct interval sums:", count_distinct_interval_sums(A))
