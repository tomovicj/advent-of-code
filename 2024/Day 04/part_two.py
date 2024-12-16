letters = []
with open("input.txt", "r") as f:
    for i in f:
        x = list(i)
        x.pop()
        letters.append(x)

def is_invalid_index_pair(index_pair):
    return index_pair[0] < 0 or index_pair[0] >= len(letters) or index_pair[1] < 0 or index_pair[1] >= len(letters[index_pair[0]])

total_found = 0
for i in range(len(letters)):
    for j in range(len(letters[i])):
        if is_invalid_index_pair((i,j)): continue
        if letters[i][j] != "A": continue

        if is_invalid_index_pair((i-1,j-1)): continue
        if is_invalid_index_pair((i+1,j+1)): continue
        a = [letters[i-1][j-1], letters[i+1][j+1]]
        a.sort()
        if a != ["M", "S"]: continue

        if is_invalid_index_pair((i-1,j+1)): continue
        if is_invalid_index_pair((i+1,j-1)): continue
        b = [letters[i-1][j+1], letters[i+1][j-1]]
        b.sort()
        if b != ["M", "S"]: continue

        total_found += 1

print(total_found)

