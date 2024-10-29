import random

def print_board(deleted,n,m):
    for i in range(n):
        for j in range(m):
            color = (i+j)%2
            if(deleted[i][j]):     
                print("  ",end='')
            else:
                if color == 1:
                    print(u'\u2592', end='')
                    print(u'\u2592', end='')
                else:
                    print(u'\u2593', end='')
                    print(u'\u2593', end='')
        print()

def random_delete(deleted,n,m,num_deletes):
    deleted_list = set()
    while len(deleted_list) < num_deletes:
        x = random.randint(0,n-1)
        y = random.randint(0,m-1)
        deleted_list.add((x,y))
    for to_delete in deleted_list:
        deleted[to_delete[0]][to_delete[1]] = True
        
def calculate_boundary(deleted,n,m):
    print()
n=5
m=5
deleted = [ [False] * n for _ in range(m)]
random_delete(deleted,n,m,10)
print_board(deleted,n,m)