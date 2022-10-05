"""A Fantasy Game inventory with a dictionary structure.
They keys are string values describing the item with integer values indicating the quantity of the item.
Write a function named displayInventory() that would take any possible inventory and display it as a list.
Include an indication of the total number of items.
Afterwards write a function named addToInventory(inventory, addedItems) where
inventory is the player's inventory and addedItems is a list.
Return a dictionary that represents the updated inventory.
"""
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory: ')
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v
    print("Total number of items: " + str(total_items))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)