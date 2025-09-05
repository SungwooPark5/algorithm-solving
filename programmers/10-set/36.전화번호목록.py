"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42577

전화번호부에서 어떤 번호가 다른 번호의 접두어가 되는 경우가 있는지 출력하는 문제
"""


def solution(phone_book):
    for n in phone_book:
        book_set = {p[: len(n)] for p in phone_book if p != n}
        if n in book_set:
            return False

    return True
