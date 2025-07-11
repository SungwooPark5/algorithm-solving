def solution(dirs):
    answer = 0

    current_loc = [0, 0]
    next_loc = [0, 0]

    paths = []

    for _, dir in enumerate(dirs):
        if dir == "U" and current_loc[1] < 5:
            next_loc[1] += 1
        elif dir == "D" and current_loc[1] > -5:
            next_loc[1] -= 1
        elif dir == "R" and current_loc[0] < 5:
            next_loc[0] += 1
        elif dir == "L" and current_loc[0] > -5:
            next_loc[0] -= 1

        if current_loc != next_loc:
            # .copy()를 하지 않고 저장할 경우, current_loc와 next_loc가 계속 변경됨
            # 따라서 값을 저장하기 위해 copy()를 사용함
            if [current_loc.copy(), next_loc.copy()] not in paths and [
                next_loc.copy(),
                current_loc.copy(),
            ] not in paths:
                answer += 1
                paths.append([current_loc.copy(), next_loc.copy()])
            current_loc = next_loc.copy()

    return answer
