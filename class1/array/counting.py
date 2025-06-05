n = int(input())

num_list = input().split()

v = int(input())

count = 0

for i in range(n):
    if int(num_list[i]) == v:
        count = count + 1

print(count)
