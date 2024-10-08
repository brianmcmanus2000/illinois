import random

def partition(array, pivot):
	to_return = ([],[])
	for i in range(len(array)):
		if array[i]<pivot:
			to_return[0].append(array[i])
		else:
			to_return[1].append(array[i])
	return to_return

def sort_union(A, B, partial_sort):
	print(A)
	print(B)
	pivot_A = random.choice(A)
	B_left, B_right = partition(B,pivot_A)
	partial_sort[len(B_left)] = pivot_A
	if len(B_left) == 1:
		partial_sort[len(B_left)-1]	= B_left[0]
	if len(B_right) == 1:
		partial_sort[len(B_left)+1]	= B_right[0]
	pivot_B = random.choice(B_left)
	A_left, A_right = partition(A,pivot_B)
	if len(A_left) == 1:
		partial_sort[len(A_left)-1]	= A_left[0]
	if len(A_right) == 1:
		partial_sort[len(A_left)+1]	= A_right[0]
	sort_union(B_left,B_right,partial_sort)
	sort_union(A_left,A_right,partial_sort)
if __name__ == "__main__": 
	A = [2, 5, 8, 12]
	B = [1, 3, 6, 10, 14]
	length = len(A)+len(B)
	final_array = [0]* length
	if len(B)>len(A): #A is always the longer list
		A, B = B, A
	sort_union(A,B,final_array)