import numpy as np

def count_distinct_interval_sums(A):
    # Compute the maximum sum M
    M = sum(A)
    
    # Define the size of the FFT array
    N = 2 * M  # Using a size that is large enough for the convolution
    
    # Initialize the polynomial representation
    P = np.zeros(N)
    P[M] = 1  # This is the polynomial 1 (constant term)
    
    for a in A:
        new_P = np.zeros(N)
        print(a)
        new_P[a:] = P[:-a]  # Shift P by `a`
        print(new_P)
        P = np.convolve(P, new_P)[:N]  # Convolve and truncate to the required size
        print(P)
    
    # Extract distinct sums from the resulting polynomial
    distinct_sums = set()
    for sum_value, count in enumerate(P):
        if count > 0:
            distinct_sums.add(sum_value)
    
    return len(distinct_sums)

# Example usage
A = [1, 2, 3]
print("Number of distinct interval sums:", count_distinct_interval_sums(A))
