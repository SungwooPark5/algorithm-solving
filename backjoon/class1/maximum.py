maximum = -1

num_list = []

for i in range(9):
    num_list.append(int(input()))

    if num_list[i] > maximum:
        maximum = num_list[i]
        index = i + 1

print(maximum)
print(index)
