"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42577

전화번호부에서 어떤 번호가 다른 번호의 접두어가 되는 경우가 있는지 출력하는 문제
"""

# 효율성 테스트를 통과하지 못한 코드 O(N^2) - 시간 초과
""" def solution(phone_book):
    for n in phone_book:
        book_set = {p[: len(n)] for p in phone_book if p != n}
        if n in book_set:
            return False

    return True
 """


# 책을 통해 startwith() 함수 사용 O(N log N) (정렬) + O(N) (for문)
def solution(phone_book):
    # 사전 순으로 정렬
    phone_book.sort()

    for p1, p2 in zip(phone_book[:-1], phone_book[1:]):
        # 다음 단어의 앞 부분이 이전 단어일 경우 접두사
        # startswith()은 O(N)의 시간 복잡도인데, 문자열 길이기 최대 20이므로 상수 시간복잡도
        if p2.startswith(p1):
            return False

    return True
