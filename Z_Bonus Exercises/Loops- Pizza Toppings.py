while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break  # Exit the loop when 'quit' is entered
    
    print(f"Adding {topping} to your pizza!")
