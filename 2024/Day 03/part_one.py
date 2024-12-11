import re

instructions = []
with open("input.txt", "r") as f:
    content = f.read()
    regex = r"mul\([\d]{1,3},[\d]{1,3}\)"
    instructions = re.findall(regex, content)

sum = 0
for i in instructions:
    nums = re.findall(r"\d+", i)
    sum += int(nums[0]) * int(nums[1])

print(sum)
