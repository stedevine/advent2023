def get_next_number(line):
    last_digits = []
    line = line.strip().split(' ')
    nums = [int(x) for x in line]
    last_digits.append(nums[-1])

    while True:
        diffs = [j-i for i, j in zip(nums[:-1], nums[1:])]
        last_digits.append(diffs[-1])
        if len(set(diffs)) == 1:
            break
        nums = diffs.copy()
            

    #print(f'nums: {nums}')
    #print(f'{last_digits} {sum(last_digits)}')

    return sum(last_digits)

def get_first_number(line):
    first_digits = []
    line = line.strip().split(' ')
    nums = [int(x) for x in line]
    first_digits.append(nums[0])
    while True:
        diffs = [j-i for i, j in zip(nums[:-1], nums[1:])]
        first_digits.append(diffs[0])
        if len(set(diffs)) == 1:
            break
        nums = diffs.copy()
    
    #print(nums)
    #print(first_digits)
    a = first_digits[-1]
    #print(a)
    for i in range(len(first_digits)-2, -1, -1):
        a = (first_digits[i] - a)
        #print(a)
        #print(f'{first_digits[i+1]} - {first_digits[i]}  = {}')
    #for i in range(0,len)
    return a

def part_1(lines):

    result = 0
    for line in lines:
        result += get_next_number(line)

    return result

def part_2(lines):

    result = 0
    for line in lines:
        result += get_first_number(line)

    return result


test="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

r = part_1(test.split('\n'))
print(f"test 1 result {r}")
r = part_2(test.split('\n'))
print(f"test 2 result {r}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")
    print(f"part 2 result {part_2(lines)}")