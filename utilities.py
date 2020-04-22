from pulp import value


def print_result(problem):
    print('Optimization status:', problem.status)
    print('Final value of the objective:', value(problem.objective))
    print('Final values of the variables:')
    for var in problem.variables():
        print(var, '=', value(var))
