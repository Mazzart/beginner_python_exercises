def greater_common_divisor(a: int, b: int) -> int:
    """Finds the largest common divisor for two numbers."""
    if b == 0:
        return a
    else:
        return greater_common_divisor(b, a % b)


def gcd(a: int, b: int) -> int:
    """Finds the largest common divisor for two numbers."""
    while a % b != 0:
        old_a = a
        old_b = b

        a = old_b
        b = old_a % old_b
    return b


if __name__ == '__main__':
    print(greater_common_divisor(120, 12))
    print(gcd(120, 12))
    print(greater_common_divisor(9, 12))
    print(gcd(9, 12))
    print(greater_common_divisor(40, 100))

