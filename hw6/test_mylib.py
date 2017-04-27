import mylib
import pytest

def test_correctval():
    assert mylib.double(1) == 2

def test_incorrectval():
    with pytest.raises(ValueError):
        mylib.double('string')