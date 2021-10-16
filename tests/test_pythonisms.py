import pytest
from pythonisms.pythonisms import LinkedList
from pythonisms.decorate_pythonisms import decorate

def test_for_in():
    ll = LinkedList(('a', 'b', 'c'))
    list = []
    for i in ll:
        list.append(i)
    assert list == ['a', 'b', 'c']

def test_equals(): 
    linkedlist1 = LinkedList([1,2,3])
    linkedlist2 = LinkedList([1,2,3])
    assert linkedlist1 == linkedlist2

def test_star():
    text = "hello"
    res = decorate(text)
    assert res == '***"hello"'


