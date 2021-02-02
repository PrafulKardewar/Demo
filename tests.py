



from unittest import mock
import pytest
from sample1 import fib


def test_fib():
    r = fib(6)
    assert r == 8