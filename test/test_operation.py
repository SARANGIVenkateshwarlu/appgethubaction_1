from src.math_operations import add,sub # functions imported 

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(10,1)==11


def test_sub():
    assert sub(5,3)==2
    assert sub(10,1)==9
    assert sub(6,3)==3
    assert sub(10,5)==5
