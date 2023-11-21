import pytest
from lib.order import *

"""
Given an instance of the order
#show_menu returns the menu
"""
def test_if_shows_menu():
    order = Order()
    result = order.show_menu()
    assert result == ['Fish and chips - £12', 'English breakfast - £10']


"""
Given an instance of the order
#build_numbered_menu returns the menu with a number for each dish
"""
def test_if_builds_numbered_menu():
    order = Order()
    assert order.build_numbered_menu() == ['1: Fish and chips - £12', '2: English breakfast - £10']


"""
Given an instance of the order and good input
#build_order expects two input numbers (food & qty) and returns the ordered food
"""
def test_if_builds_order_input13():
    order = Order()
    order.build_numbered_menu()
    assert order.build_order() == ['3x Fish and chips - £36'] # input 13


"""
Given an instance of the order and good input
#build_order expects two input numbers (food & qty) and returns the ordered food
"""
def test_if_builds_order_input24():
    order = Order()
    order.build_numbered_menu()
    assert order.build_order() == ['4x English breakfast - £40'] # input 24


"""
Given an instance of the order and wrong item input
#build_order expects two input numbers (food & qty) and returns the ordered food
"""
def test_if_builds_order_wrong_item_input():
    order = Order()
    order.build_numbered_menu()
    with pytest.raises(Exception) as e: 
        order.build_order() # input 01 or any wrong item input
    error_message = str(e.value)
    assert error_message == "There is no item menu with that number"


"""
Given an instance of the order and wrong quantity input
#build_order expects two input numbers (food & qty) and returns the ordered food
"""
def test_if_builds_order_wrong_qty_input():
    order = Order()
    order.build_numbered_menu()
    with pytest.raises(Exception) as e: 
        order.build_order() # input 10 or any wrong quantity input
    error_message = str(e.value)
    assert error_message == "Wrong quantity, you can only order minimum 1 and maximum 5 of each item"