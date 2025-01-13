from error import square


def testSquarePass():
    assert square(2) == 4


def testSquareFail():
    assert square(2) == 2
