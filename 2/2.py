# Limit is 12 red, 13 green, 14 blue

# input : 
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

def process_round(round):
    r = 0
    g = 0 
    b = 0
    cubes = round.split(',')
    for cube in cubes:
        cube = cube.strip()
        if 'red' in cube:
            r = int(cube.split(' red')[0])
        if 'blue' in cube:
            b = int(cube.split(' blue')[0])
        if 'green' in cube: 
            g = int(cube.split(' green')[0]) 

    return (r,g,b)

def get_max_per_game(lines):
    game_result = []
    for line in lines:
        max_red = 0 
        max_green = 0
        max_blue = 0
        line = line.strip()


        game_number = int(line.split('Game ')[1].split(':')[0])
        rounds = line.split('Game ')[1].split(':')[1].strip().split(';')

        for round in rounds:
            round_result = process_round(round)
            max_red = max(max_red, round_result[0])
            max_green = max(max_green, round_result[1])
            max_blue = max(max_blue, round_result[2])
    
        game_result.append((game_number, max_red, max_green, max_blue))    

    return game_result


def part_1(lines):
    result = 0
    for game_result in get_max_per_game(lines):
        game_number, red, green, blue = game_result
        if red <= 12 and green <= 13 and blue <= 14:
            result += game_number
    
    return result

def part_2(lines):
    result = 0
    for game_result in get_max_per_game(lines):
        _, red, green, blue = game_result
        result += (red * green * blue)

    return result


test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

test1_result = part_1(test.split('\n'))
print(f"test 1 result {test1_result}")
test2_result = part_2(test.split('\n'))
print(f"test 2 result {test2_result}")

with open('./input.txt') as f:
    lines = f.readlines()

    print(f"part 1 result {part_1(lines)}")
    print(f"part 2 result {part_2(lines)}")
