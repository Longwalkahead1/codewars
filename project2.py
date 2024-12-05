"""Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.


"""
items = ["apples", "oranges", "bannanas", "pears"]
def add_item (item):
    items.append(item)
def sub_items (item):
 items.remove(item)

def main ():
     while True:
        print("1 add, 2 remove, 3 list")  
        option=input("what option would you like to select? ")
        if option == "1":
            item = input("what is the item? ")
            add_item(item)
            print("item added succesfully!")
        elif option == "2":
           item = input("what is item? ")
           sub_items(item)
           print("item remove succesfully!")
        elif option == "3":
           print(f"here are the grocerries from your list! {items}")
main()


