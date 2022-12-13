def findItem(rucksack):
    rucksack = rucksack[:-1]
    compartment_size = int(len(rucksack)/2)
    
    for i in range(compartment_size):
        for j in range(compartment_size):
            if rucksack[i] == rucksack[compartment_size+j]:
                return rucksack[i]

input = open("input.txt", "r")
rucksacks = input.readlines()
priorities_sum = 0

for rucksack in rucksacks:
    priority = 0
    item = findItem(rucksack)
    if ord(item) <= 90:
        priority = ord(item)-38
    else:
        priority = ord(item)-96
    priorities_sum += priority
    
print(priorities_sum)