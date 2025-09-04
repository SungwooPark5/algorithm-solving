"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/12981

끝말잇기에서 탈락한 사람의 번호와 순서를 출력하는 문제
중복된 단어를 말하거나, 이전 단어의 마지막 글자로 시작하는 단어를 말하지 못할 경우 탈락
set()을 이용하여 중복된 단어를 검사하고, 글자가 이어지는 지도 검사해야 함
아래 코드보다 더 짧게 작성할 수 있으니 책을 보고 참고하기
"""


def solution(n, words):
    spoken_words = set()
    count = -1

    for i, word in enumerate(words):
        if i == 0:
            spoken_words.add(word)
            continue

        previous_word = words[i - 1]

        if word in spoken_words or previous_word[-1] != word[0]:
            count = i
            break

        spoken_words.add(word)

    print(count)

    if count == -1:
        answer = [0, 0]
    else:
        num = (count) % n + 1
        order = (count) // n + 1
        answer = [num, order]

    return answer
