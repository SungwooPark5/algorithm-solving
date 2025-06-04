sum_list = []

while True:
    a, b = input().split()

    a = int(a)
    b = int(b)

    if (a == 0) and (b == 0):
        break
    else:
        sum_list.append(a + b)

for i in range(len(sum_list)):
    print(sum_list[i])
