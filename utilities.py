from pulp import value


def print_result(problem):
    print('Optimization status:', problem.status)
    print('Final value of the objective:', value(problem.objective))
    print('Final values of the variables:')
    for var in problem.variables():
        print(var, '=', value(var))

        
def print_power_values(problem, p, appliances, time_steps):
    print("\t".join(['Time'] + ['App' + str(i) for i in appliances]))
    for t in time_steps:
        print("\t".join([str(t)] + [str(int(value(p[(i, t)]))) for i in appliances]))