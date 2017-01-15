import os
import pytest

from unittest.mock import MagicMock
from modA import modA


@pytest.fixture(scope='function')
def write_file(request):
    """ This fixture creates a file with given request
    as parameters (fname, text)"""
    fname, text = request.params
    with open(fname, 'w') as f :
        f.write(text)
    yield fname
    os.remove(fname)


@pytest.mark.parametrize('write_file', 
        [("filename.txt", "Content\nTo\nWrite\n")],
        indirect=True)
def test_write_file(monkeypatch, write_file):
    fname = write_file
    with open(fname,'r') as f:
        for line in f:
            print(line)


def test_modA_behaviour(monkeypatch, write_file):
    monkeypatch.setattr("modB.modB.B1",MagicMock(return_value = "x"))
    monkeypatch.setattr("modB.modB.B2",MagicMock(return_value = "x"))
    myobj=modA()
    assert before_test_create_dataset == "coucou"
    assert myobj.A1()=="A1 x"
    assert myobj.A2()=="A2 x"
