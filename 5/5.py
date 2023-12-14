def part_1(lines):  
    seeds, maps = parse_input(lines)
    return process_seeds(seeds,maps)

def part_2(lines):

    seeds, maps = parse_input(lines)
    all_seeds = set()
    for i in range(0, len(seeds)//2):
        #for i in range(0, 1):
        idx = i*2
        #print(f'{seeds[idx]} {seeds[idx+1]}'  )
        for j in range(seeds[idx], seeds[idx]+seeds[idx+1],1000):
            #print(process_seeds([j],maps))
            all_seeds.add(j)
    
    #print(all_seeds)
    return process_seeds(all_seeds,maps)
    #print(f'all_seeds: {all_seeds}')

def process_seeds(seeds,maps):
    results = []
    for seed in seeds:
        soil = get_mapped_value(maps['seed-to-soil'], seed)
        #print(f'seed {seed} -> {soil}')
        fert = get_mapped_value(maps['soil-to-fertilizer'], soil)
        #print(f'soil {soil} -> {fert}')
        water = get_mapped_value(maps['fertilizer-to-water'], fert)
        light = get_mapped_value(maps['water-to-light'], water)
        temp = get_mapped_value(maps['light-to-temperature'], light)
        humid = get_mapped_value(maps['temperature-to-humidity'], temp)
        loc = get_mapped_value(maps['humidity-to-location'], humid)
        results.append(loc)
        print(f'{seed} -> {loc}')
    #print(results)
    results.sort()
    return results[0]

def parse_input(lines):
     # parse out the seeds and the maps
    seeds = lines[0].split(': ')[1].split(' ')
    seeds = [int(i) for i in seeds if i !='']
    #print(seeds)
    maps = {}
    for idx in range(1,len(lines)):
        line = lines[idx].strip()
        if line == '':
            continue
        #print(line)
        if 'map' in line:
            current_map = line.split(' map:')[0]
            maps[current_map] = []
        else:
            maps[current_map].append([int(i) for i in line.split(' ')])

    return (seeds, maps)

def get_mapped_value(map, key):
    for line in map:
        #print(f'{line[0]} : {line[0] + line[2] -1}')
        lo = line[1]
        hi = line[1] + line[2] - 1
        if key >= lo and key <= hi:
            #print('mapped')
            v = line[0] + key - line[1]
            return v
            #print(f'{key} -> {v}')

    return key

test="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

test1_result = part_1(test.split('\n'))
print(f"test 1 result {test1_result}")

test2_result = part_2(test.split('\n'))
print(f"test 2 result {test2_result}")

with open('./input.txt') as f:
    lines = f.readlines()

    #print(f"part 1 result {part_1(lines)}")
    print(f"part 2 result {part_2(lines)}")