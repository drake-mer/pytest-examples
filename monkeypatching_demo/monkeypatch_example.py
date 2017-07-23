# coding: utf-8
"""
Just Run:
    `pytest monkeypatch_example.py`
    
to launch the test
"""

import pytest

from os import linesep
try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock



class B():
    def B1(self):
        return "This string is going to be monkeypatched"
    def B2(self):
        return "This string is into modB class, staying"


class A():
    def __init__(self):
        self.b_obj = B()

    def A1(self):
        return "Our A() type object, calling B.B1:" \
        + linesep + self.b_obj.B1()

    def A2(self):
        return "Our A() object, calling B.B2:" \
        + linesep + self.b_obj.B2()



def test_monkeypatch(monkeypatch):
    """ Simple test function to demonstrate the monkeypatching process """

    # Instanciate the objects we are going to use
    clear_object = A()

    # Use class methods before monkeypatching
    print("Before monkeypatching")
    clear_object.A1()
    clear_object.A2()


    # what is going on after monkeypatching ?
    print("After monkeypatching")
    mock_object = MagicMock( return_value = "You just have been monkeypatched. Please keep going" )
    monkeypatch.setattr( B, "B1", mock_object )
    patched_object = A()
    patched_object.A1()  # must call module_to_monkeypatch.modB.B1 (which is actually monkeypatched)
    patched_object.A2()  # must call module_to_monkeypatch.modB.B2 (which the initial commited method)

    assert mock_object.called
    assert mock_object.call_count == 1

    n_repeat = 10
    for x in range(n_repeat):
        my = patched_object.A1()

    assert mock_object.call_count == 1 + n_repeat



