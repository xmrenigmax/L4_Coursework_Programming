def restock_inventory(available_items, inventory_records, current_day):
    # Check if there are any inventory records available for reference 
    # Get the available items from the last record in the inventory records list
    # If no records of available items, set available items to 0
    if inventory_records:
        available_items = inventory_records[-1][3]
    else:
        available_items = 0

    # Initialize restocked_units to 0 for the current day
    restocked_units = 0

    # Check if the current day is a restocking day (every multiple of 7)
    # Restock inventory to maximum capacity of 2000 units
    if current_day % 7 == 0:
        available_items = 2000

    # Calculate restocked units based on the last available items
    # If there are previous records, calculate the difference to 2000
    # If no previous records, all 2000 units are restocked
        if inventory_records:
            restocked_units = 2000 - inventory_records[-1][3]
        else:
            restocked_units = 2000
        
    # Update inventory records for the current day with restocked units
        inventory_records.append([current_day, 0, restocked_units, available_items])
    # Return the available items
    return available_items

