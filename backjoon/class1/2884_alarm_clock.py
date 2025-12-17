EARLY = 45

H, M = [int(x) for x in input().split()]

def HM_to_minute(hour, minute):
    return hour*60 + minute

def minute_to_HM(minute):
    if minute < 0:
        minute = 24*60 + minute
    hour = minute // 60
    return f"{hour} {minute - hour*60}"

early_minute = HM_to_minute(H, M) - EARLY

print(minute_to_HM(early_minute))