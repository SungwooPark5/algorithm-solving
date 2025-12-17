T = int(input())

H, W, N = [0]*T, [0]*T, [0]*T

for i in range(T):
    H[i], W[i], N[i] = [int(x) for x in input().split()]
    

for i in range(T):
    if N[i] % H[i] == 0:
        room_num = N[i] // H[i]
        room_stair = H[i]
    else:
        room_num = N[i] // H[i] + 1
        room_stair = N[i] % H[i]
    
    room = room_stair*100 + room_num
    
    print(room)