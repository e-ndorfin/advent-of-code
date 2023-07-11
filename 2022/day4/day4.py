with open('day4.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# Task 1
# count = 0
# for pair in data:
#     elf1, elf2 = pair.split(',')
#     elf1 = [int(i) for i in elf1.split('-')]
#     elf2 = [int(i) for i in elf2.split('-')]
#     if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
#         count += 1
#     elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
#         count += 1

# print(count)

# Task 2
count = 0
for pair in data:
    elf1, elf2 = pair.split(',')
    elf1 = [int(i) for i in elf1.split('-')]
    elf2 = [int(i) for i in elf2.split('-')]
    if elf1[0] in range(elf2[0], elf2[1]+1) or elf1[1] in range(elf2[0], elf2[1]+1):
        count += 1
    elif elf2[0] in range(elf1[0], elf1[1]+1) or elf2[1] in range(elf1[0], elf1[1]+1):
        count += 1


print(count)
