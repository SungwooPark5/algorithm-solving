t = int(input())

sum_list = []

for i in range(t):
    a, b = input().split()

    sum_list.append(int(a) + int(b))

for i in range(t):
    print(sum_list[i])
