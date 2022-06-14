def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    assert isinstance(s, list)
    s.reverse()
    return s


if __name__ == "__main__":
    test_s = ["h", "e", "l", "l", "o"]

    print(f"{test_s} translate to {reverseString(test_s)}")
