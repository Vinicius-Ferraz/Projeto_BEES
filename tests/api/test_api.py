import requests


BASE_URL="https://test-bees.herokuapp.com"


def setup_module(module):
    """setup any state specific to the execution of the given module."""
    pass

def teardown_module(module):
    """teardown any state that was previously setup with a setup_module
    method.
    """
    pass

def setup_function(function):
    """setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    pass

def teardown_function(function):
    """teardown any state that was previously setup with a setup_function
    call.
    """
    pass

def test_01():
    r = requests.get(url=f'{BASE_URL}/deposits.json',timeout=5)
    assert r.status_code == 200
    

def test_02():
    r = requests.post(url=f'{BASE_URL}/deposits.json',data=
    {"name": "teste",
    "address": "teste",
    "city": "teste",
    "state": "teste",
    "zipcode": "teste"
    })
    assert r.status_code == 201
    

def test_03():
    pass