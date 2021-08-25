def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = v + item_total

    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 1)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)