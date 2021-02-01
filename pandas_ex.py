









import time

def compute(x):
    response = response_api_call()
    return response + x

def response_api_call():
    time.sleep(1000)
    return 123

def test_compute():
    expected = 124
    actual = compute(1)
    assert expected == actual