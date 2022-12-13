def findItem(r1, r2, r3):    
    for i in range(len(r1)):
        for j in range(len(r2)):
            for k in range(len(r3)):
                if(r1[i] == r2[j] == r3[k]):
                    return r1[i]

input = open("input.txt", "r")
rucksacks = input.readlines()
priorities_sum = 0

for elf in range(0, len(rucksacks), 3):
    r1 = rucksacks[elf]
    r2 = rucksacks[elf+1]
    r3 = rucksacks[elf+2]
    priority = 0
    item = findItem(r1, r2, r3)
    if(ord(item) <= 90):
        priority = ord(item)-38
    else:
        priority = ord(item)-96
    priorities_sum += priority
    
print(priorities_sum)