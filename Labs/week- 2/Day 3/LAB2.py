total_items = 17
box_capacity = 5

full_box = total_items // box_capacity
remaining_items = total_items % box_capacity

print(f"You can fill up to: {full_box}")
print(f"And you will have {remaining_items} remaining")