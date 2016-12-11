import pytest

from mock import MagicMock
from modA import modA


# -- Fixture that will create data set before each test
@pytest.fixture()
def before_test_create_dataset(request):
    with open('test1','w') as f :
        f.write('hello1')
        yield "coucou"



# -- Fixture that will remove data set after each test
@pytest.fixture()
def after_test_remove_dataset( request ):
    def _remove_dataset():
        pass
    request.addfinalizer( _remove_dataset )
    
def test_modA_behaviour(monkeypatch,before_test_create_dataset):
    monkeypatch.setattr("modB.modB.B1",MagicMock(return_value = "x"))
    monkeypatch.setattr("modB.modB.B2",MagicMock(return_value = "x"))
    myobj=modA()
    assert before_test_create_dataset == "coucou"
    assert myobj.A1()=="A1 x"
    assert myobj.A2()=="A2 x"
