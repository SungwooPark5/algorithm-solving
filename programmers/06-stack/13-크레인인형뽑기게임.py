def solution(board, moves):
    answer = 0

    stack = []
    pick = 0

    for move in moves:
        # move(column)에 해당하는 인형 뽑기
        for row in range(len(board)):
            if board[row][move - 1] != 0:
                pick = board[row][move - 1]
                board[row][move - 1] = 0
                break

        # 인형을 stack에 저장하기
        if len(stack) != 0 and stack[-1] == pick:
            answer += 2
            stack.pop()
        elif pick != 0:
            stack.append(pick)

        pick = 0

    return answer
