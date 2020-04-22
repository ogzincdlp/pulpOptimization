from pulp import LpProblem, LpMinimize, LpVariable, value


#%% Simple Linear Optimization

# problem definition with name and 'sense'
problem = LpProblem('Simple Minimization', LpMinimize)

# Variables are defined with names, bounds, and categories
x = LpVariable('x', lowBound=0, cat='Continuous')
y = LpVariable('y', upBound=5, cat='Integer')

# the objective is added to the problem as a statement
problem += 3*x - 5*y

# the constraints are added as conditionals
problem += y <= x

problem.solve()

# problem status is 1 if optimized
print(problem.status)
for var in problem.variables():
    print(var, '=', value(var))
