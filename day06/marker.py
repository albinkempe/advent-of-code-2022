input = open("input.txt", "r")
data = input.readlines()[0]
last_chars = [0 for _ in range(14)]

i = 0
for c in data:
    last_chars[i % 14] = c
    if len(last_chars) <= len(set(last_chars)) and i > 13:
        break
    i += 1

print(i+1)