#include <iostream>
#include <vector>

int main() {
    int total_value, no_of_cars;
    std::cin >> total_value;
    std::cin >> no_of_cars;

    std::vector<int> car_array(no_of_cars + 1);
    for (int i = 1; i <= no_of_cars; i++) {
        std::cin >> car_array[i];
    }

    // DP matrix to store valid states, initialized to 0 (false)
    std::vector<std::vector<int>> matrix(no_of_cars + 1, std::vector<int>(total_value + 1, 0));
    // Array to track whether each car went to the left or right lane
    std::vector<std::vector<int>> direction(no_of_cars + 1, std::vector<int>(total_value + 1, -1));

    matrix[0][0] = 1;  // Start state: No cars placed and no weight on the left lane

    int total_till_now = 0;
    int max_loaded = 0;  // To track how many cars were actually loaded
    int max_left_weight = -1;  // To track the left lane's final weight

    // Fill the DP table
    for (int i = 1; i <= no_of_cars; i++) {
        total_till_now += car_array[i];
        for (int j = 0; j <= total_value; j++) {
            if (matrix[i - 1][j] == 1) {
                // Can the current car go to the left lane?
                if (j + car_array[i] <= total_value) {
                    matrix[i][j + car_array[i]] = 1;
                    direction[i][j + car_array[i]] = 0;  // Car goes to the left lane
                }
                // Can the current car go to the right lane?
                int right = total_till_now - j;
                if (right <= total_value) {
                    matrix[i][j] = 1;
                    direction[i][j] = 1;  // Car goes to the right lane
                }
            }
        }
    }

    // Find the maximum number of cars that can be loaded
    for (int j = 0; j <= total_value; j++) {
        if (matrix[no_of_cars][j] == 1) {
            max_loaded = no_of_cars;
            max_left_weight = j;
            break;
        }
    }

    // If no valid configuration was found, print 0
    if (max_left_weight == -1) {
        std::cout << "0\n";
        return 0;
    }

    // Output the number of cars loaded
    std::cout << max_loaded << "\n";

    // Backtrack to find the placement of each car (left or right)
    std::vector<char> result;
    int k = max_left_weight;  // Start with the final left lane weight

    for (int i = max_loaded; i > 0; i--) {
        if (direction[i][k] == 0) {
            result.push_back('L');
            k -= car_array[i];  // Reduce the left lane weight by the car's weight
        } else {
            result.push_back('R');
        }
    }

    // Output the results in reverse order (since we backtracked)
    for (int i = result.size() - 1; i >= 0; i--) {
        std::cout << result[i] << "\n";
    }

    return 0;
}
