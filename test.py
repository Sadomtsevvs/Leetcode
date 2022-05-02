from unittest.mock import Mock, MagicMock
from collections import Counter

mocked_form = Mock()
mocked_form.validate.return_value = True
mocked_form.name.data = 'test name'
mocked_form.address.data = 'test address'

print(mocked_form.validate())
print(mocked_form.name.data)
print(mocked_form.address.data)
print(type(mocked_form.address.data))

class TestName:
    data = 'test name'

class TestAddress:
    data = 'test address'

class MockedOrderForm:

    name = TestName()
    address = TestAddress()

    def validate(self):
        return True

mocked_form = MockedOrderForm()
print(mocked_form.validate())
print(mocked_form.name.data)
print(mocked_form.address.data)
print(type(mocked_form.address.data))

cntr = Counter('ffe')
print(bool(cntr))
cntr['f'] -= 2
del cntr['f']
cntr['e'] -= 1
del cntr['e']
print(bool(cntr))