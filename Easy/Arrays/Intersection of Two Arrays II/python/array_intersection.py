def intersect(nums1, nums2):
    """
    Return intersection of arrays of integers nums1 and nums2
    :param nums1: array of integer
    :param nums2: array of integer
    :return: array intersection of nums1 and nums2
    """

    nums1.sort()
    nums2.sort()
    ans = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            ans.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
    return ans


def intersect_oneliner(nums1, nums2):
    """
    Return intersection of arrays of integers nums1 and nums2
    :param nums1: array of integer
    :param nums2: array of integer
    :return: array intersection of nums1 and nums2
    """

    assert isinstance(nums1, list)
    assert isinstance(nums2, list)
    assert 1 <= len(nums1) <= 1000
    assert 1 <= len(nums2) <= 1000

    result = []
    for element in nums1:
        if element in nums2:
            result.append(element)
            nums2.remove(element)
    return result


if __name__ == "__main__":
    num1 = [4, 9, 5]
    num2 = [9, 4, 9, 8, 4]
    print(intersect(num1, num2))
    print(intersect_oneliner(num1, num2))
