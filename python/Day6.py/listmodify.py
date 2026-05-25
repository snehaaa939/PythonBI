# Books details are stored as [harry_potter, lord_of_rings, harry_potter, ...]
# Find the position of first occurrence of harry_potter
# Remove the first occurrence of harry_potter and display the list
# Ask user for a book name and check if its present in list
# Add the_hobbit to the end of list and display it
# Insert game_of_thrones at index 2 and display the list
# Count and display how book for lord_of_rings is present in the list
# Remove book from 2nd position. Display removed book and original list
# Display the total number of books in the list
# Display all books of list separated by comma
# Assign book_2 as [math, science, history]. Add all books from it to above list and display.
# Sort the list in descending order based on length of book name and display result.

book_list = ["harry_potter", "lord_of_rings", "harry_potter", "narnia"]

# Find the position of first occurrence of harry_potter
print("First occurrence of harry_potter:", book_list.index("harry_potter"))

# Remove the first occurrence of harry_potter and display the list
book_list.remove("harry_potter")
print("After removing first harry_potter:", book_list)

# Ask user for a book name and check if its present in list
book_name = input("Enter a book name:")
book_present = book_list.index(book_name)
print(f"book is present in the book_list.")

# # Add the_hobbit to the end of list and display it
book_list.append("the_hobbit")
print(book_list)

# Insert game_of_thrones at index 2 and display the list
book_list.insert(2, "game_of_thrones")
print(book_list)

# Count and display how book for lord_of_rings is present in the list
book_count = book_list.count("lord_of_rings")
print(f"The number of lord_of_rings book present in the list is {book_count}.")

# Remove book from 2nd position. Display removed book and original list
book_remove = book_list.pop(2)
print(f"The removed book is {book_remove}.")
print(book_list)

# Display the total number of books in the list
total_books = len(book_list)
print(f"The total number of books in the list is: {total_books}.")

# Display all books of list separated by comma
print(", ".join(book_list))

# Assign book_2 as [math, science, history]. Add all books from it to above list and display.
book_2 = ["math", "science", "history"]
book_list.extend(book_2)
print(book_list)

# Sort the list in descending order based on length of book name and display result.
desc_sort = book_list.sort(reverse=True)
print(book_list)
book_list.sort(key=len)
print(book_list)
