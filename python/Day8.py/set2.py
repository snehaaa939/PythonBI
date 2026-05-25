# Q. Store list as ["book", "book", "pen", "pen", "pen", "pencil", "marker", "notebook"]
# Save unique items sold in stationary shop in a set as unq_items_set and display the result
# Find and display total number of unique items sold in stationary shop
# Add sticky_notes to unq_items_set set and display updated set
# Remove pen from unq_items_set set and display updated set
# Check if stapler is present in unq_items_set set and display result
# Remove eraser from unq_items_set and display result. Shouldn't give error if not present
# Assign new_items as ["highlighter", "chart_paper"]. Add all items from new_items to unq_items_set and display updated set

items_list = ["book", "book", "pen", "pen", "pen", "pencil", "marker", "notebook"]
# Save unique items sold in stationary shop in a set as unq_items_set and display the result
unique_items = set(items_list)
print("Unique items sold in stationary shop:", unique_items)

# Find and display total number of unique items sold in stationary shop
total_unique_items = len(unique_items)
print("Total number of unique items:", total_unique_items)

# Add sticky_notes to unq_items_set set and display updated set
unique_items.add("sticky_notes")
print("After adding sticky_notes:", unique_items)

# Remove pen from unq_items_set set and display updated set
unique_items.remove("pen")
print("After removing pen:", unique_items)

# Check if stapler is present in unq_items_set set and display result
is_stapler_present = "stapler" in unique_items
print("Is stapler present?", is_stapler_present)

# Remove eraser from unq_items_set and display result. Shouldn't give error if not present
unique_items.discard("eraser")
print("After attempting to remove eraser:", unique_items)

# Assign new_items as ["highlighter", "chart_paper"]. Add all items from new_items to unq_items_set and display updated set
new_items = ["highlighter", "chart_paper"]
unique_items.update(new_items)
print("After adding new items:", unique_items)