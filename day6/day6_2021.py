import pathlib
import math

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = [int(i) for i in f.read().strip().split(',')]
    return lines

def part1(data):
    days = 18
    for i in range(days):
        for j in range(len(data)):
            if(int(data[j]) == 0):
                data[j] = 6
                data.append(8)
            else:
                data[j] -= 1
    return len(data)

def part2(data, nday):
    days = [0] * 9
    for fish in data:
        days[fish] += 1
    for i in range(nday):
        new_fish = days[0]
        for i in range(8):
            days[i] = days[i+1]
        days[6] += new_fish
        days[8] = new_fish
    return sum(days)

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part2(data[:], 80)
    solution2 = part2(data[:], 256)
    return solution1, solution2

if __name__ == '__main__':
    puzzle_input = PUZZLE_DIR / 'input.txt'
    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))