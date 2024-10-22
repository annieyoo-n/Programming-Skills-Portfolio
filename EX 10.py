

#Exercise 10:Is it even?

def check_even_odd(number):
    # Determine if the number is even or odd
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    # Enter any number
    number = int(input("Enter a number: "))
    
    # Pass the number to the function and get the result
    result = check_even_odd(number)
    
    # Print the message returned by the function
    print(result)

if __name__ == "__main__":
    main()
