def process_rule(part, rule, rule_map):
    #print(f'rule : {rule}')
    # understand the rule
    k = rule[0]
    op = rule[1]
    val = rule[2:].split(":")[0]
    then = rule[2:][len(val):]
    #print(f'{k} {op} {val} {then} || {part}')
    #print(part)

    # apply the operation
    if op == '<':
        result = 0 if part[k] < int(val) else 1
    elif op == '>':
        result = 0 if part[k] > int(val) else 1
    else:
        print("error")
        return

    # process the 'then' statement based on the result
    # to see what we do next
    if result == 0:
        next = then.split(',')[0]
    else:
        next = then[len(then.split(',')[0]):]
    next = next[1:]
    #print(f'next {next}')

    if next == 'A':
        #print(f'Accepted {part}')
        return part.get('x',0) + part.get('m','0') + part.get('a', 0) + part.get('s', 0)
    elif next == 'R':
        #print(f'Reject {part}')
        return 0
    elif ':' in next:
        return process_rule(part, next, rule_map)
    else:
        return process_rule(part, rule_map[next], rule_map)


def part_1(lines):
    # process the rules
    rule_map = {}
    line_index = 0
    for line_index in range(0, len(lines)):
        line = lines[line_index]
        if len(line) < 2:
            break
        rule_name, rule = line.strip().split('{')
        rule_map[rule_name] = rule[:-1]
    
    #print(rule_map)
    parts = []
    line_index += 1
    for part_index in range(line_index, len(lines)):
        part = {}
        line = lines[part_index]
        line = line.split("{")[1].split("}")[0]
        #print(line)
        sub_parts = line.split(',')
        for sub in sub_parts:
            k,v = sub.split('=')
            part[k] = int(v)
        parts.append(part)

    final_result = 0 
    for i in range(0, len(parts)):
        #final_result += process_part(parts[i], rule_map)
        final_result += process_rule(parts[i], rule_map['in'], rule_map)
        #print(process_part(parts[i], rule_map))

    #print(process_part(parts[4], rule_map))
    return final_result


test="""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


r = part_1(test.split('\n'))
print(f"test result {r}")
r = part_1(test.split('\n'))
print(f"test result {r}")

with open('./input.txt') as f:
    lines = f.readlines()
    print(f"part 1 result {part_1(lines)}")