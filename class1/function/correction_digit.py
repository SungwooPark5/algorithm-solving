def get_correction_number(num_list: list[int]) -> int:

    result = 0

    for n in num_list:
        result += n * n
        # ^ 기호는 제곱이 아닌 비트 연산임!

    result = result % 10

    return result


serial_num = list(input().split())
serial_num = [int(x) for x in serial_num]

print(get_correction_number(serial_num))
