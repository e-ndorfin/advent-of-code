# Getting data
with open('day1.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# print(data)


# Part 1
# max = 0
# temp = 0

# for num in data:
#     if num != '':
#         temp += int(num)
#     else:
#         if temp > max:
#             max = temp
#         temp = 0

# print(max)

# Part 2


top = [0, 0, 0]
temp = 0

for num in data:
    if num != '':
        temp += int(num)
    else:
        if temp > top[0]:
            top[2] = top[1]
            top[1] = top[0]
            top[0] = temp
        elif temp > top[1]:
            top[2] = top[1]
            top[1] = temp
        elif temp > top[2]:
            top[2] = temp
        temp = 0

print(top)
print(sum(top))
