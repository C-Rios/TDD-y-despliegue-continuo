from functions import minValue

def test_minValue():
    assert minValue([1,2,3,4,5]) == 1
    assert minValue([5,3,9,7,0,9]) == 0
    assert minValue([-10,5,0,-9,3,5]) == -10
    assert minValue([15,20,30,385,12]) == 12
    assert minValue([7,8,9,10,11]) == 7
    assert minValue([5,6,90,25,6,9]) == 5