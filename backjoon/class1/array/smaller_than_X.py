n, x = input().split()

n = int(n)
x = int(x)

char_list = input().split()

for i in range(n):
    if int(char_list[i]) < x:
        print(char_list[i], end=" ")
