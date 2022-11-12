def numbers(a: int) -> str:
    string_numbers = {0: 'zero',
                      1: 'one',
                      2: 'two',
                      3: 'three',
                      4: 'four',
                      5: 'five'}
    return string_numbers.get(a)


# num = numbers(4)
# print(num)
