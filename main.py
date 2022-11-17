import random
from datetime import datetime
from ortools.algorithms import pywrapknapsack_solver
from random import randint
from timeit import default_timer as timer


# def timer(option):
#
#     if option == "start":
#         start_time = datetime.now()
#
#     if option == "end":
#         end_time = datetime.now()
#         print('Duration: {}'.format(end_time - start_time))


def branch_and_bound(values, weights, capacities):

    solver = pywrapknapsack_solver.KnapsackSolver(pywrapknapsack_solver.KnapsackSolver.
                                                  KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'Branch and bound')
    solver.Init(values, weights, capacities)
    start = timer()
    result = solver.Solve()
    end = timer()
    print('Duration: {}'.format(end-start))
    output(result, solver, values, weights)

def dynamic(values, weights, capacities):
    solver = pywrapknapsack_solver.KnapsackSolver(pywrapknapsack_solver.KnapsackSolver.
                                                  KNAPSACK_DYNAMIC_PROGRAMMING_SOLVER, 'Dynamic')
    solver.Init(values, weights, capacities)
    start = timer()
    result = solver.Solve()
    end = timer()
    print('Duration: {}'.format(end - start))
    output(result, solver, values, weights)


def greedy(values, weights, capacities):
    total_weight = 0
    cap = capacities[0]
    solution = []
    for (w, v) in zip(weights[0], values):
        if total_weight+w < cap:
            total_weight += w
            solution.append([w, v])
        else:
            break




def output(computed_value, solver, values, weights):
    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)
    print('-'*50)


def main():
    rand_values = [randint(1, 50) for p in range(0, 10000)]
    rand_weights = [[randint(10, 100) for p in range(0, 10000)]]

    values = [
        360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
        312]

    weights = [[
        7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
    ]]
    capacities = [10000]

    branch_and_bound(rand_values, rand_weights, capacities)
    dynamic(rand_values, rand_weights, capacities)
    greedy(rand_values, rand_weights, capacities)

    # Create the solver.
    # solver = pywrapknapsack_solver.KnapsackSolver(
    #     pywrapknapsack_solver.KnapsackSolver.
    #     KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    #
    # solver.Init(values, weights, capacities)
    # start_time = datetime.now()
    # computed_value = solver.Solve()
    # end_time = datetime.now()
    #
    # output(computed_value, solver, values, weights)
    # print('Duration: {}'.format(end_time - start_time))
    # packed_items = []
    # packed_weights = []
    # total_weight = 0
    #
    # print('Total value =', computed_value)
    # for i in range(len(values)):
    #     if solver.BestSolutionContains(i):
    #         packed_items.append(i)
    #         packed_weights.append(weights[0][i])
    #         total_weight += weights[0][i]
    # print('Total weight:', total_weight)
    # print('Packed items:', packed_items)
    # print('Packed_weights:', packed_weights)
    #
    # branch_and_bound(values, weights, capacities)
    # dynamic(values, weights, capacities)


if __name__ == '__main__':
    main()
