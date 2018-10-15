def greater_common_divisor(a, b):
    '''Finds the largest common divisor for two numbers.'''
    if b == 0:
        return a
    else:
        return greater_common_divisor(b, a % b)


if __name__ == '__main__':
    print(greater_common_divisor(120, 12))
    print(greater_common_divisor(9, 12))
    print(greater_common_divisor(40, 100))

