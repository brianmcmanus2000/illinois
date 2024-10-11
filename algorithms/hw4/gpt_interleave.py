import random

def interleave_sort(A, B):
    def partition(A, B, lo, hi):
        if lo > hi:
            return
        if(lo==hi==0):
            return
        
        pivot_A = random.choice(A[lo:hi+1])
        pivot_B = random.choice(B[lo:hi+1])
        #print("pivot_A = "+str(pivot_A)+", pivot_B = "+str(pivot_B))
        #print("A pre-partition:")
        #print(A)
        partition_index_A = partition_based_on_B(A, lo, hi, pivot_B)
        #print("A post-partition:")
        #print(A)
        interleaved[2 * partition_index_A] = pivot_A
        partition(A, B, lo, partition_index_A - 1)
        partition(A, B, partition_index_A + 1, hi)

        partition_index_B = partition_based_on_A(B, lo, hi, pivot_A)
        interleaved[2 * partition_index_B + 1] = pivot_B
        partition(A, B, lo, partition_index_B - 1)
        partition(A, B, partition_index_B + 1, hi)
        

    # Helper function to partition B based on pivot_A
    def partition_based_on_B(A, lo, hi, pivot_B):
        i = lo
        j = hi
        print(A)
        print("i="+str(i)+", j="+str(j)+", pivot_B="+str(pivot_B))
        while i <= j:
            # If B[i] is less than pivot_A, it's on the correct side
            if A[i] < pivot_B:
                i += 1
                print("element i="+str(i)+" was smaller than pivot")
            # If B[j] is greater than pivot_A, it's on the correct side
            elif A[j] > pivot_B:
                j -= 1
                print("element j="+str(j)+" was larger than pivot")
            # If B[i] is greater and B[j] is smaller, swap them
            else:
                print("got here 1")
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        
        # Return the partition index
        # We need to return the correct index for the element from B that will
        # alternate with pivot_A in the interleaved array
        return i - 1 if i > lo else i
    def partition_based_on_A(B, lo, hi, pivot_A):
        i = lo
        j = hi
        
        while i <= j:
            # If B[i] is less than pivot_A, it's on the correct side
            if B[i] < pivot_A:
                i += 1
            # If B[j] is greater than pivot_A, it's on the correct side
            elif B[j] > pivot_A:
                j -= 1
            # If B[i] is greater and B[j] is smaller, swap them
            else:
                print("got here 2")
                B[i], B[j] = B[j], B[i]
                i += 1
                j -= 1
        
        # Return the partition index
        # We need to return the correct index for the element from B that will
        # alternate with pivot_A in the interleaved array
        return i - 1 if i > lo else i
    
    # Prepare the interleaved array of size 2n (for perfect interleaving)
    n = len(A)
    interleaved = [None] * (2 * n)
    
    # Step 5: Call the recursive partitioning function
    partition(A, B, 0, n - 1)
    
    return interleaved


# Example usage
A = [3, 1, 5,7]
B = [4, 2, 6,8]

# Call the interleaving sort function
sorted_interleaved_array = interleave_sort(A, B)
print(sorted_interleaved_array)
