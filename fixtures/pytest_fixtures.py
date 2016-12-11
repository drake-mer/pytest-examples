import sys
import pytest
import itertools


@pytest.yield_fixture( scope="function" )
def create_abc_fixture(request, monkeypatch):
    a,b,c=request.param
    yield a,b,c


@pytest.mark.parametrize(
    "create_abc_fixture",
    list( itertools.product(
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9)
        )
    ),
    indirect=['create_abc_fixture'] )
def test_abc_fixture(create_abc_fixture):
    a,b,c = create_abc_fixture
    assert a*b*c in list(range(1,9*6*3+1))
    assert not a*b*c > 9*6*3
    assert not a*b*c < 1
    if a*b*c == 28:
        # you know prime decomposition of 28 is 7 × 2 × 2
        # so this is always true in the context of our tests
        assert a==1
        assert b==4
        assert c==7
    sys.stderr.write("{},{},{}".format(a,b,c))
