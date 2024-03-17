import pytest


def test_float1():
    assert float('3.0') == 3.0


def test_float2():
    assert abs(0.1 + 0.2 - 0.3) < 1e-9


def test_float3():
    with pytest.raises(ValueError):
        assert float('example')
    
    
@pytest.mark.parametrize('test_set, element', [({1, 2, 3}, 2), 
                                               ({'a', 'b', 'c'}, 'a'), 
                                               ({10, 20, 30}, 50)])
def test_set1(test_set, element):
    assert (element in test_set) == (element in test_set)


def test_set2():
    assert {1, 2, 3, 1, 2} == {1, 2, 3}


def test_set3():
    assert {1, 2, 3}.union({4, 5, 6}) == {1, 2, 3, 4, 5, 6}
    