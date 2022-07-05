import pytest
from mypkg.dummy_class import dummy_class

def test_foo(
    example_dummy: dummy_class,
) -> None:
    '''Test foo'''
    assert example_dummy is not None