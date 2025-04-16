import pytest
import functions.my_functions as my_func

def test_add():
    result=my_func.add(1,5)
    assert result==6

def test_divide():
    
    result=my_func.divide(6,3)
    assert result==2    

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_func.divide(20,0)    