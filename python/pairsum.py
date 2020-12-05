from itertools import combinations

arr = list(map(int, input().split()))
k = int(input())
count = 0
for i in combinations(arr, 2):
    if sum(i) == k:
        count += 1
print(count)