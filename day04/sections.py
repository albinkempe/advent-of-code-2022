input = open("input.txt", "r")
section_assignments = input.readlines()

overlaps = 0

for pair in section_assignments:
    temp = pair.split(",")
    elf1 = temp[0].split("-")
    elf2 = temp[1].split("-")
    
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]) or int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        overlaps += 1
        
print(overlaps)