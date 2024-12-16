import random

def rolls_to_hit(N):
    overall_count = 0
    for _ in range(N):
        target = random.randint(1,100)
        guess = -1
        count = 0
        while guess != target:
            count+=1
            guess = random.randint(1,100)
        overall_count+=count
    print(f"average number of rolls to hit target: {overall_count/N}")


def run_n_times(N):
    overall_count = 0
    for _ in range(N):
        count = 0
        seats = list(range(100))
        professor_seat = random.randint(0, 99)  
        seats.remove(professor_seat)  
        for i in range(1, 100):
            if professor_seat == i:  
                count += 1
                professor_seat = random.choice(seats)  
                seats.remove(professor_seat) 
            else:
                seats.remove(i)  
        overall_count += count
    
    print(f"Average number of times moved: {overall_count / N}")

def move_once(N):
    overall_count = 0
    for _ in range(N):
        count = 0
        seats = list(range(100))
        professor_seat = random.randint(0, 99)  
        seats.remove(professor_seat)  
        for i in range(1, 100):
            if professor_seat == i:  
                count += 1
                professor_seat = random.choice(seats)  
                seats.remove(professor_seat) 
            else:
                seats.remove(i)  
        if(count==1):
            overall_count += 1
    print(f"chance professor moved once: {overall_count/N}")

# run_n_times(100000)
# rolls_to_hit(10000)
move_once(10000000)