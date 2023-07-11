# Reading data
with open('day3.in') as file:
    data = [i for i in file.read().strip().split('\n')]


def find_letter_index(s, target):
    for i, letter in enumerate(s):
        if letter == target:
            return i


# Task 1
# score = 0
# alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for rucksack in data:
#     half_index = len(rucksack) // 2
#     compartment_1 = rucksack[:half_index]
#     compartment_2 = rucksack[half_index:]

#     for letter in compartment_1:
#         if letter in compartment_2:
#             temp_score = find_letter_index(alphabet, letter)
#             score += temp_score + 1
#             break

# print(score)

# Task 2

score = 0
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(0, len(data), 3):
    for letter in data[i]:
        if letter in data[i+1] and letter in data[i+2]:
            score += find_letter_index(alphabet, letter) + 1
            break
print(score)


# for rucksack in data:
#     half_index = len(rucksack) // 2
#     compartment_1 = rucksack[:half_index]
#     compartment_2 = rucksack[half_index:]
