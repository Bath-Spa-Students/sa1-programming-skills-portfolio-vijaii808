# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function to get user input and print the result
def main():
    # Ask the user for a number
    user_input = int(input("Please enter a number: "))
    
    # Pass the number to the check_even_odd function
    result = check_even_odd(user_input)
    
    # Print the result returned from the function
    print(result)

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()