def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Code to reverse the fruit list
    fruit_list.reverse()
    print(fruit_list)

    # Code to append orange to the list
    fruit_list.append("orange")
    print(fruit_list)

    # Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the
    #  list and print the list
    fruit_list.insert(1, "cherry")
    print(fruit_list)
    
    # Code to remove banana from the list
    fruit_list.remove("banana")
    print(fruit_list)

    # Add code to pop the last element from fruit_list
    #  and print the popped element and the list.
    fruit_list.pop(4)
    print(fruit_list)

    # code to sort fruit list
    sorted_list=sorted(fruit_list)
    print(sorted_list)

    # code to clear the whole list
    fruit_list.clear()
    print(fruit_list)

main()
