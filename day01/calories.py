input_file = open("input.txt", "r")
input = input_file.readlines()

calories = []
temp = 0
for i in range(len(input)+1):
    if i == len(input) or input[i] == '\n':
        calories.append(temp)
        temp = 0
    else:
        temp += int(input[i])

calories.sort()
print(calories[-1])
print(calories[-1]+calories[-2]+calories[-3])