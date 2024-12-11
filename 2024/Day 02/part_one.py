def is_safe(levels):
    way = None
    for i in range(len(levels) - 1):
        a = int(levels[i])
        b = int(levels[i + 1])
        x = a - b
        if x == 0 or x > 3 or x < -3: return False
        if way is None:
            if x < 0:
                way = "increasing"
                continue
            way = "decreasing"
            continue
        if (way == "increasing" and x > 0) or (way == "decreasing" and x < 0): return False
    return True

reports = []
with open("input.txt", "r") as f:
    for i in f:
        levels = i.split(" ")
        reports.append(levels)

total_safe_reports = 0
for i in reports:
    if is_safe(i):
        total_safe_reports += 1
        
print(total_safe_reports)
