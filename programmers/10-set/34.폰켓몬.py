"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

N/2의 몬스터를 선택할 수 있을 때, 최대한 많은 종류의 몬스터를 출력하는 경우, 최대 종류의 수를 출력하는 문제
python의 set을 이용하여 간단하게 중복되지 않는 집합을 만들 수 있음
set()의 시간 복잡도는 O(N)임.
"""


def solution(nums):
    answer = 0
    select_num = len(nums) / 2

    type_num = len(set(nums))

    if type_num > select_num:
        return select_num
    else:
        return type_num
