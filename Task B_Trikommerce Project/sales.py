import random

def daily_sales(available_items, inventory_records, current_day):

    # Check if there are any inventory records available
    if current_day % 7 != 0 and current_day != 0:

        #Random number of sold units up to 200
        sold_units = random.randint(0, 200)

        #Updates available items
        available_items = available_items - sold_units

        # updates inventory records with number of units sld and remaining inventory
        inventory_records.append([current_day, sold_units, 0, available_items])
        
    # Return the updated available items
    return available_items
