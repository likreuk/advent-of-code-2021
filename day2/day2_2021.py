import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = f.read().splitlines()
    return lines

def part1(data):
    horizontal = 0
    depth = 0
    for i in data:
        position = i.split(' ')
        if position[0] == 'forward':
            horizontal += int(position[1])
        elif position[0] == 'down':
            depth += int(position[1])
        elif position[0] == 'up':
            depth -= int(position[1])
    final = horizontal * depth 
    return final

def part2(data):
    #Part 2
    horizontal = 0
    depth = 0
    aim = 0
    for i in data:
        position = i.split(' ')
        if position[0] == 'forward':
            horizontal += int(position[1])
            depth += aim * int(position[1])
        elif position[0] == 'down':
            aim += int(position[1])
        elif position[0] == 'up':
            aim -= int(position[1])
    return horizontal * depth 

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == '__main__':
    puzzle_input = PUZZLE_DIR / 'input.txt'
    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))