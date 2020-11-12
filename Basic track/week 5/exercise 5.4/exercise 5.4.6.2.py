def add_fruit(inventory, fruit, quantity=0):
    """
    >>> new_inventory = {}
    >>> add_fruit(new_inventory, 'strawberries', 10)
    >>> print('strawberries' in new_inventory))
	True
    >>> print(new_inventory["strawberries"] == 10)
    True
    >>> add_fruit(new_inventory, 'strawberries', 25)
    >>> print(new_inventory['strawberries'])
    35
    """
    if inventory.has_key(fruit):
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

import doctest

doctest.testmod()
