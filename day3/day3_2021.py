import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = f.read().splitlines()
    return lines

def ep_gam(data):
    count = [0] * len(data[0])
    for i in data:
        temp = 0
        for j in i:
            if(int(j) == 1):
                count[temp] = count[temp] + 1
            temp += 1
    gamma = ''
    epsilon = ''
    for i in count:
        if(i >= len(data)/2):
            epsilon = epsilon[:] + '1'
            gamma = gamma[:] + '0'
        else:
            gamma = gamma[:] + '1'
            epsilon = epsilon[:] + '0'
    return epsilon, gamma

def part1(data):
    epsilon, gamma = ep_gam(data)
    print('epsilon ', epsilon)
    print('gamma ', gamma)
    return int(epsilon, 2) * int(gamma, 2)

def oxy_gen_rating(data):
    temp = 0
    while(len(data)>1):
        epsilon, gamma = ep_gam(data)
        for i in data[:]:
            if(int(epsilon[temp]) != int(i[temp])):
                data.remove(i)
        temp +=1
    return int(data[0],2)
    #for i in data:

def co_rating(data):
    temp = 0
    while(len(data)>1):
        epsilon, gamma = ep_gam(data)
        for i in data[:]:
            if(int(epsilon[temp]) == int(i[temp])):
                data.remove(i)
        temp +=1
    return int(data[0],2)

def part2(data):
    oxy = oxy_gen_rating(data[:])
    co = co_rating(data[:])    
    return oxy * co

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == '__main__':
    puzzle_input = PUZZLE_DIR / 'input.txt'
    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))