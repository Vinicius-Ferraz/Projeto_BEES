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
    pass

def test_02():
    pass

def test_03():
    pass