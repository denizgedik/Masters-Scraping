with open('masters.txt') as f:
    lines = f.readlines()
    f.close()

new_list = []
number = 1
for line in lines:
    if (number % 2) == 0:
        pass
    elif line[0] == '"':
        pass
    else:
        line.strip()
        new_line = '"' + line.strip() + '", \n'
        new_list.append(new_line)
    number += 1

with open('better_masters.txt', 'w') as f:
    for line in new_list:
        f.write(line)
    f.close()