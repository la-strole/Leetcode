from timeit import timeit
from random import randint

def containsDuplicate(nums: list) -> bool:
    """
    Return True if elements in nums array not duplicates - else return False
    """
    
    assert isinstance(nums, list)
    assert 1 <= len(nums) <= pow(10, 5)
    for n in nums:
        assert isinstance(n, int)
        assert pow(-10, 9) <= n <= pow(10, 9)

    return len(set(nums)) != len(nums)

def containsDuplicate_v2(nums: list) -> bool:
    """
    Return True if elements in nums array not duplicates - else return False
    """
    
    assert isinstance(nums, list)
    assert 1 <= len(nums) <= pow(10, 5)
    for n in nums:
        assert isinstance(n, int)
        assert pow(-10, 9) <= n <= pow(10, 9)

    c = dict()
    
    for number in nums:
        # if number in c.keys - they are hashed 
        if number in c:
            return True
        else:
            # add number to c.keys
            c[number] = 1
    return False

if __name__ == "__main__":

    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    '''
    # test time speed
    
    print(f"time_v_1: {timeit('containsDuplicate([randint(-pow(10, 9), pow(10,9)) for _ in range(randint(1,pow(10,5)))])', globals = globals(), number=pow(10, 2))}")
    print(f"time_v_2: {timeit('containsDuplicate_v2([randint(-pow(10, 9), pow(10,9)) for _ in range(randint(1,pow(10,5)))])', globals = globals(), number=pow(10, 2))}")
    '''
    print(containsDuplicate(test_array))
    print(containsDuplicate_v2(test_array))