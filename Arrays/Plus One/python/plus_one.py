def plusOne(digits):
    i = -1
    while i >= -len(digits):
        if digits[i] + 1 < 10:
            digits[i] += 1
            break
        else:
            digits[i] = 0
            i -= 1
    else:
        digits.insert(0, 1)

    return digits


if __name__ == "__main__":
    test_array = [1, 9, 1, 1, 1, 1]
    print(plusOne(test_array))
