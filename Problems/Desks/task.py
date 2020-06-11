from math import ceil

group1 = int(input())
group2 = int(input())
group3 = int(input())
print(sum((ceil(group1 / 2), ceil(group2 / 2), ceil(group3 / 2))))
