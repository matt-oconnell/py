from hw6.attrType.AttrType import AttrType
import pytest

def test_value_sets_str_correctly():
    type = AttrType(str)
    type.a = 'abc'
    assert type.a == 'abc'

def test_value_sets_int_correctly():
    type = AttrType(int)
    type.a = 123
    assert type.a == 123

def test_value_throws_error():
    type = AttrType(str)
    with pytest.raises(ValueError):
        type.a = 123

def test_overwrite():
    type = AttrType(str)
    type.a = 'abc'
    type.a = 'xyz'
    assert type.a == 'xyz'

def test_write_once():
    type = AttrType(str, True)
    type.a = 'abc'
    with pytest.raises(ValueError):
        type.a = 'xyz'

def test_as_list():
    type = AttrType(str)
    type.a = 'abc'
    type.b = 'xyz'
    assert type.as_list() == ['a', 'b']

def test_as_dict():
    type = AttrType(str)
    type.a = 'abc'
    type.b = 'xyz'
    assert type.as_dict() == { 'a': 'abc', 'b': 'xyz' }