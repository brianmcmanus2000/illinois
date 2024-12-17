import numpy as np

from scipy.optimize import linprog



# Define the payoff matrix M for the Undercut game (example: 6x6 matrix)


M = np.array([

    [0,  -3, 2, 3, 4],

    [3,  0,  -5, 2, 3],

    [-2, 5,  0,  -7, 2],

    [-3,  -2, 7,  0,  -9],

    [-4,  -3,  -2, 9,  0]
])
M = np.array([

    [0,  1, -2, -3, -4, -5],

    [-1,  0,  3, -2, -3, -4],

    [2, -3,  0,  5, -2, -3],

    [3,  2, -5,  0,  7, -2],

    [4,  3,  2, -7,  0,  9],

    [5,  4,  3,  2, -9,  0]

])

# Number of strategies (n)

n = M.shape[0]

# Adjusting the linear programming setup to ensure correctness

# Constraints need to enforce that z is a lower bound on Alex's expected payoff
# Revisiting the formulation to correct the LP

# Objective: max z (or equivalently min -z in linprog)
c = [-1] + [0] * n  # Minimize -z

# Constraints for the expected payoff: z <= a^T M
A_ub = np.hstack((np.ones((n, 1)), -M.T))  # Column for z, rest for a
b_ub = [0] * n  # Expected payoff constraints

# Equality constraint: sum of probabilities is 1
A_eq = np.hstack(([0], np.ones(n))).reshape(1, -1)  # Sum of a_i = 1
b_eq = [1]

# Bounds for variables
bounds = [(None, None)] + [(0, 1)] * n  # z is unbounded, a_i are probabilities

# Solve the linear program again
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Extract the optimal strategy and game value if successful
if result.success:
    z_star = -result.fun  # Optimal game value
    a_star = result.x[1:]  # Alex's optimal strategy
else:
    z_star = None
    a_star = None

z_star, a_star
print(z_star)
print(a_star)