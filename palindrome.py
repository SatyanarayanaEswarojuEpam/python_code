def is_string_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def is_number_palindrome(number):
    # Convert number to string and check if it's palindrome
    return str(number) == str(number)[::-1]

def main():
    # Test string palindrome
    text = input("Enter a string to check for palindrome: ")
    if is_string_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")
    
    # Test number palindrome
    try:
        number = int(input("\nEnter a number to check for palindrome: "))
        if is_number_palindrome(number):
            print(f"{number} is a palindrome!")
        else:
            print(f"{number} is not a palindrome.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()