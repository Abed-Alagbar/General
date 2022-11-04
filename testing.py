#1- write the code and hope it works

def adds_two_numbers(a,b):
    return a + b
    
    
# write the test and hope it passess
   
def test_adds_two_numbers():
    a=5
    b=5
    expected = 10
    actual = adds_two_numbers(a,b)
    assert actual == expected ,'Only positive numbers are allowed'

test_adds_two_numbers()
