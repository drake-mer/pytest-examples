# coding: utf-8

import sys
import pytest
import itertools


@pytest.yield_fixture( scope="function" )
def abc_fixture(request, monkeypatch):
    """ This is a parametrized fixture that returns a tuple (a,b,c) """
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
def test_use_abc_fixture(abc_fixture):
    """ This test function uses the abc_fixture defined above 
    (a,b,c) is in { 1, 2, 3 } × { 4, 5, 6 } × { 7, 8, 9 }
    
    So basically (a,b,c) is in { (1, 4, 7), (1, 4, 8), ..., (3, 6, 9) }
    
    Thus (a*b*c) product lies between (4*7)=28 and (3*6*9)=162
    """
    a,b,c = create_abc_fixture
    assert a*b*c in list(range(1,9*6*3+1))
    assert not a*b*c > 9*6*3
    assert not a*b*c < 28
    if a*b*c == 28:
        # each (a,b,c) is unique so there is a bijection 
        # between 
        # the set { (a*b*c) | a in {1,2,3}, b in {4,5,6}, c in {7,8,9} } and 
        # the set { (a,b,c) | a in {1,2,3}, b in {4,5,6}, c in {7,8,9} }
        assert a==1
        assert b==4
        assert c==7
        
