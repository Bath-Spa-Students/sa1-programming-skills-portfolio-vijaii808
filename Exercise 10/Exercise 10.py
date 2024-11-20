def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    user_input = int(input("Enter a number: "))
    result = check_even_odd(user_input)
    print(result)

if __name__ == "__main__":
    main()