def part_1(lines):
    result = 0
    for line in lines:
        line = line.strip()
        digits = list(filter(lambda a: a.isdigit(),line))
        result += int(digits[0])*10 + int(digits[-1])

    return result


def part2(lines):
    digit_map = {
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }

    parsed_lines = []
    for line in lines:
        line = line.strip()
        for k,v in digit_map.items():
            # need to preserve the value and insert the integer -> oneightwo -> one1oneight8eightwo2two
            line = line.replace(k, k + str(v) + k)
            #print(line)
        parsed_lines.append(line)

    return part_1(parsed_lines)


part_2_test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

print(part2(part_2_test.split('\n')))

#print(part2(['oneightwo']))

with open('./input.txt') as f:
    lines = f.readlines()

    print(f"part 1 result {part_1(lines)}")
    print(f"part 2 result {part2(lines)}")


"""

def part_2(lines):
    result = 0 
    digits = [str(i) for i in range(1,10)]
    digits += ['one','two','three','four','five','six','seven','eight','nine']
    for line in lines:
        first = {}
        last = {}
        line = line.strip()
        # Find the position of the digit in the line
        for digit in digits:
            if digit in line:
                idx = digits.index(digit)
                # get the value from the digit
                if idx < 9:
                    val = idx + 1
                else:
                    val = idx - 8
                first[line.find(digit)] = val 
                last[line.rfind(digit)] = val 
        
        result += first[min(first)]*10 + last[max(last)]
    return result
"""