def load_cars_inefficiently(ferry_capacity, cars):
    lanes = [0, 0, 0]  # Initialize the weight in each of the 3 lanes
    assignments = []    # Track which lane each car is assigned to

    for car in cars:
        assigned = False  # To track if the car was assigned successfully

        # Try to assign the car to the least loaded lane that can fit the car
        for i in range(3):
            # Find the lane with the least weight that can still accommodate the car
            min_index = lanes.index(min(lanes))
            
            if lanes[min_index] + car <= ferry_capacity:
                lanes[min_index] += car
                assignments.append(min_index + 1)  # Store the lane number (1-based)
                assigned = True
                break  # Car assigned, break the loop

            # If the car doesn't fit in any of the lanes, it can't be loaded
        if not assigned:
            print(f"Car with weight {car} could not be assigned to any lane without exceeding capacity.")
            break

    return lanes, assignments


# Test the function
ferry_capacity = 6
cars = [3,3,4,4,2,2] 

lanes, assignments = load_cars_inefficiently(ferry_capacity, cars)

# Output the final lane assignments and their respective loads
print("Final lane loads:", lanes)
print("Car assignments:", assignments)
