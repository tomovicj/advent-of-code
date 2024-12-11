listR = []
listL = []

with open("input.txt") as f:
    for i in f:
        [r, l] = i.split("   ")
        listR.append(int(r))
        listL.append(int(l))

dictL = {}
for i in listL:
    if i not in dictL:
        dictL[i] = 0
    dictL[i] += 1

total_similarity_score = 0
for i in listR:
    l = 0
    if i in dictL:
        l = dictL[i]
    total_similarity_score += i * l

print(total_similarity_score)