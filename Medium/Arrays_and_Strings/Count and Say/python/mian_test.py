import pytest
from main import Solution


def test_main():
    n = 1
    assert Solution().countAndSay(n) == '1'

    n = 4
    assert Solution().countAndSay(n) == "1211"
    n = 3
    assert Solution().countAndSay(n) == "21"
    n = 4
    assert Solution().countAndSay(n) == "1211"
    n = 5
    assert Solution().countAndSay(n) == "111221"
    n = 6
    assert Solution().countAndSay(n) == "312211"
    n = 7
    assert Solution().countAndSay(n) == "13112221"
    n = 8
    assert Solution().countAndSay(n) == "1113213211"
    n = 9
    assert Solution().countAndSay(n) == "31131211131221"
    n = 10
    assert Solution().countAndSay(n) == "13211311123113112211"
