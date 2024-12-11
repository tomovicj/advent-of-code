listR = []
listL = []
with open("input.txt") as f:
    for i in f:
        [r, l] = i.split("   ")
        listR.append(int(r))
        listL.append(int(l))

listR.sort()
listL.sort()

total_distance = 0
for i in range(len(listR)):
    distance = listR[i] - listL[i]
    if (distance < 0):
        distance *= -1
    total_distance += distance

print(total_distance)