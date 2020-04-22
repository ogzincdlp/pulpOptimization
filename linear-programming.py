from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable, value, lpDot

from utilities import print_result

# %% Simple Linear Optimization

# problem definition with name and 'sense'
problem = LpProblem('Simple Minimization', LpMinimize)

# Variables are defined with names, bounds, and categories
x = LpVariable('x', lowBound=0, cat='Continuous')
y = LpVariable('y', upBound=5, cat='Integer')

# the objective is added to the problem as a statement
problem += 3 * x - 5 * y

# the constraints are added as conditionals
problem += y <= x

problem.solve()

# problem status is 1 if optimized
print_result(problem)

# %% Declaring a list of variables
# This is an example of maximizing utility with cost constraint problem

# Assume we have a list of variables (x1, x2, x3, x4)
variable_names = [1, 2, 3, 4]

# Cost of each variables is defined in a dictionary
costs = {
    1: 0.05,
    2: 0.02,
    3: 0.07,
    4: 0.09
}

# Similarly utilities are defined in a dictionary
utilities = {
    1: 10,
    2: 8,
    3: 15,
    4: 20
}

# Variables are defined as a dictionary with comman bounds and category
# variables is a dictionary with keys being the elements of the variable_names list
# Values of this dict is the variable names (X_1, X_2...) which can be referred to
# define objectives and constraints
variables = LpVariable.dict('X', variable_names,
                            lowBound=0, upBound=20, cat='Continuous')

problem = LpProblem('Maximize Utility', LpMaximize)

# Objective is defined as a dot product of the variables and corresponding utilities
problem += lpDot(variables.values(), utilities.values())

# Similarly, total cost is defined as the dot product of variables and costs
problem += lpDot(variables.values(), costs.values()) <= 1

problem.solve()

print_result(problem)

