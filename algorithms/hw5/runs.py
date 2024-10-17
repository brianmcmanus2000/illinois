import random,math

def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
         
    return(key1)
def count_runs(str): 
    length = len(str)
    run_length = int(math.log2(length))+1
    counter = 0
    ones = "1"*run_length
    zeros = "0"*run_length
    for i in range(0,length-run_length):
        if str[i:i+run_length] == ones:
            counter+=1
        elif str[i:i+run_length] == zeros:
            counter+=1
    return counter
n = 128
counter = 0
num_trials = 10000
for i in range(num_trials):
    str1 = rand_key(n)
    counter += count_runs(str1)
average = counter/num_trials
print("There are on average "+str(average)+" runs of length "+str(math.log2(len(str1))+1)+" in a string of length "+str(n))