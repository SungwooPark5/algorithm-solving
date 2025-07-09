def solution(answers):
    answer = []

    correct_num = [0, 0, 0]

    answer1 = [i % 5 + 1 for i in range(len(answers))]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    for i in range(len(answers)):
        if answer1[i] == answers[i]:
            correct_num[0] += 1
        if answer2[i] == answers[i]:
            correct_num[1] += 1
        if answer3[i] == answers[i]:
            correct_num[2] += 1

    max_correct = max(correct_num)

    for i in range(3):
        if correct_num[i] == max_correct:
            answer.append(i + 1)

    return answer
