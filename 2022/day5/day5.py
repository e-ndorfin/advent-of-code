import re

with open('day5.in') as file:
    data = [i for i in file.read().split('\n')]

# class Stack():

# Task 1
# starting = data[:9]
# commands = data[10:]

starting = data[:9]
commands = data[10:]

# makes a stack for each number listed in line 9
stacks = {int(digit): [] for digit in starting[-1].replace(' ', '')}

# splits and adds each letter into each stack
for line in starting[:-1]:
    lst = []
    for i in range(0, len(line)):
        if line[i] not in ['[', ']', ' ']:
            stacks[(i+3)/4] += line[i]

# reverses each stack for easy popping
for lst in stacks:
    stacks[lst].reverse()


for command in commands:
    # stupid formatting of the instructions to leave the instructions
    command = command.strip('move ')
    command = command.split()
    # format of command: ['1', 'from', '3', 'to', '9']
    move_num, starting_num, ending_num = int(
        command[0]), int(command[2]), int(command[4])
    for i in range(0, move_num):
        stacks[ending_num] += stacks[starting_num].pop()

# stacks[starting_num].pop()

ans = ""
for stack in stacks:
    ans += str(stacks[stack].pop())
print(ans)

# move 1 from 8 to 4
# move 1 from 7 to 8
# move 1 from 6 to 3

# for letter in line:

#     if letter not in :
#         enumerate

# starting = [i.split('  ') for i in starting]
# for lst in starting:
#     lst = [i.strip('[] ') for i in lst]
# print(starting)

# starting = [i.split(' ') for i in starting]
# print(starting)
# starting = [i.strip('[] ') for i in starting]
# print(starting)
