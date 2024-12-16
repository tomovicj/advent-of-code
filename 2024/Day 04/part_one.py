def look_for(i, j, y, x, n):
    if n >= len(word):
        return True
    c = word[n]

    i = i+y
    j = j+x

    if i >= len(letters) or j >= len(letters[i]): return False
    if i < 0 or j < 0: return False
    
    if letters[i][j] != c: return False

    return look_for(i, j, y, x, n+1)

letters = []
with open("input.txt", "r") as f:
    for i in f:
        x = list(i)
        x.pop()
        letters.append(x)

word = "XMAS"
total_found = 0
for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j] != word[0]: continue

        for y in range(-1, 2):
            for x in range(-1, 2):
                if look_for(i, j, y, x, 1):
                    total_found += 1

print(total_found)

