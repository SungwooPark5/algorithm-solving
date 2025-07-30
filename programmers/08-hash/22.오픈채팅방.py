def solution(record):
    answer = []
    nickname_dict = {}
    message = []

    # 최종 nickname_dict 생성
    for r in record:
        message = r.split(" ")

        if message[0] == "Enter" or message[0] == "Change":
            nickname_dict[message[1]] = message[2]

        message = []

    # 최종 메시지 출력
    for r in record:
        message = r.split(" ")

        nickname = nickname_dict[message[1]]

        if message[0] == "Enter":
            answer.append(f"{nickname}님이 들어왔습니다.")
        elif message[0] == "Leave":
            answer.append(f"{nickname}님이 나갔습니다.")

    return answer
