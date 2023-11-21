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
#build_numbered_menu displays the menu with a number for each dish
"""
def test_if_builds_numbered_menu():
    order = Order()
    assert order.build_numbered_menu() == ['1: Fish and chips - £12', '2: English breakfast - £10']


"""
Given an instance of the order
#order_food expects two input numbers (food & qty) and returns the ordered food
"""
def test_if_orders_food():
    order = Order()
    assert order.build_numbered_menu() == ['1: Fish and chips - £12', '2: English breakfast - £10']
    assert order.order_food(3) == ['3x Fish and chips - £12']
