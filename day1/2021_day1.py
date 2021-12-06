import pandas as pd
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = f.read().splitlines()
    return lines

def part1(data):
    previous = 0
    count = -1
    for i in data:
        if int(i) > previous:
            count += 1
        previous = int(i)
    return count

def part2(data):
    df = pd.DataFrame(data, columns=['data'])
    previous = 0
    count = -1
    for index, row in df.iterrows():
        if(index < 2):
            continue
        else:
            first = df['data'].loc[index-2]
            second = df['data'].loc[index-1]
            third = df['data'].loc[index]
            s = int(first) + int(second) + int(third)
        if s > previous:
            count = count + 1
        previous = s
    return count

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == '__main__':
    puzzle_input = PUZZLE_DIR / 'input.txt'
    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))
