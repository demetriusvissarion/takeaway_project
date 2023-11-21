import pytest
from unittest.mock import Mock
from lib.receipt import *

"""
Given an instance of the receipt
#confirmation_message returns a confirmation message
"""
def test_if_confirmation_message():
    order =  Mock()
    order.build_numbered_menu.return_value == ['1: Fish and chips - £12', '2: English breakfast - £10']
    order.order_food(3).return_value == ['3x Fish and chips - £12']
    receipt = Receipt(order.order_food(3))
    result = receipt.confirmation_message()
    assert result == "Thank you! Your order was placed and will be delivered before 18:52"