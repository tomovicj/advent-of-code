import re

instructions = []
with open("input.txt", "r") as f:
    content = f.read()
    patterns = [
        r"mul\([\d]{1,3},[\d]{1,3}\)",
        r"do\(\)",
        r"don't\(\)",
    ]
    ordered_matches = []
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            ordered_matches.append((match.start(), match.group()))
        
    # Sort by position and extract only the matches
    instructions = [m[1] for m in sorted(ordered_matches)]

sum = 0
enabled = True
for i in instructions:
    if i == "don't()":
        enabled = False
        continue
    if i == "do()":
        enabled = True
        continue
    if enabled:
        nums = re.findall(r"\d+", i)
        sum += int(nums[0]) * int(nums[1])

print(sum)
