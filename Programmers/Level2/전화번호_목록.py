def solution(phone_book):
    phone_set = set()
    for number in phone_book:
        phone_set.add(number)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[: i] in phone_set:
                return False
    return True