def solution(arr1, arr2):
    answer = [[]]

    answer = [[0 for _ in enumerate(arr2[0])] for _ in enumerate(arr1)]

    for i, _ in enumerate(arr1):
        for j, _ in enumerate(arr2[0]):
            for k, _ in enumerate(arr2):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer
