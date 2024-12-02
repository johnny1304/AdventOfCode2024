def part_one():
    r_list = []
    l_list = []
    with open('resources/input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split('   ')
            l_list.append(int(parts[0]))
            r_list.append(int(parts[1].strip('\n')))

    l_list.sort()
    r_list.sort()
    total = 0
    for i in range(len(l_list)):
        total += abs(l_list[i] - r_list[i])

    print(total)

def part_two():
    r_list = []
    l_list = []
    r_occurences = {}
    with open('resources/input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split('   ')
            l_list.append(int(parts[0]))
            r_list.append(int(parts[1].strip('\n')))

            if not r_occurences.__contains__(parts[1].strip('\n')):
                r_occurences[parts[1].strip('\n')] = int(1)
            else:
                count = r_occurences.get(parts[1].strip('\n'))
                r_occurences[parts[1].strip('\n')] = int(count)+int(1)
        l_list.sort()
        total = 0
        for i in range(len(l_list)):
            if r_occurences.__contains__(str(l_list[i])):
             total += abs(l_list[i] * r_occurences[str(l_list[i])])

        print(total)

part_two()