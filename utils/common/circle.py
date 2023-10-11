
def circle(now: int, tot: int):
    if now > tot - 1:
        return 0
    if now == tot - 1:
        return 0
    return now + 1
