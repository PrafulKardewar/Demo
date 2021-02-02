




from unittest import mock


m=mock.Mock()
assert isinstance(m.foo,mock.Mock)
assert isinstance(m.bar,mock.Mock)
assert isinstance(m(),mock.Mock)
assert m.foo is not m.bar is not m()

m.foo = 'bar'
assert m.foo=='bar'
m.configure_mock(bar='baz')
assert m.bar=='baz'

m.return_value =45
assert m() ==45
m.side_effect=['foo','bar','doo']


assert m()=='foo'
assert m()=='bar'
assert m()=='doo'
m.side_effect= RuntimeError
try:
    m()
except RuntimeError:
    assert True
else:
    assert False



