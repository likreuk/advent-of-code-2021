import pathlib
import math
import statistics

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = [int(i) for i in f.read().strip().split(',')]
    return lines

def part1(data):
    print(statistics.median(data))
    high = max(data)
    fuel = []
    for i in range(high+1):
        cost = 0
        for j in data:
            cost += abs(i-j)
        fuel.append(cost)
    return min(fuel)


def part2(data):
    high = max(data)
    step_cost = [i for i in range(high + 1)]
    fuel = []
    for i in range(high+1):
        cost = 0
        for j in data:
            change = abs(i-j)
            cost += sum(step_cost[0:change+1])
        fuel.append(cost)
    return fuel[fuel.index(min(fuel))]

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data[:])
    solution2 = part2(data[:])
    return solution1, solution2

if __name__ == '__main__':
    puzzle_input = PUZZLE_DIR / 'input.txt'
    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))