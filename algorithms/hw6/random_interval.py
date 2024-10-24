import numpy as np

def generate_intervals(n):
    # Generate n random points uniformly distributed in [0,1]
    points = np.random.uniform(0, 1, n)
    
    # Sort the points
    sorted_points = np.sort(points)
    intervals = []
    intervals.append(sorted_points[0])
    for i in range(len(sorted_points)-1):
        intervals.append(sorted_points[i+1]-sorted_points[i])
    intervals.append(1-sorted_points[-1])
    return intervals

def harmonic(n:float):
    acc=0
    for i in range(n):
        acc+=1/(i+1)
    return acc

i = 0
acc=0
num_samples = 100000
num_points = 100
while i<num_samples:
    intervals = generate_intervals(num_points)
    acc+=max(intervals)
    i+=1
average = acc/num_samples
print(average)
print(harmonic(num_points)/(num_points+1))