import random
import string


def generate_password(length):
    """Function to generate a password of specified length"""
    letters = string.ascii_letters
    numbers = string.digits
    # remove single quote to avoid errors in SQL queries
    symbols = string.punctuation.replace("'", "")
    password = "".join(random.choice(letters + numbers + symbols)
                       for _ in range(length))
    return password


def main():
    """Main function to get user input and generate password."""
    length = int(
        input("Enter the length of the password you want to generate : "))
    password = generate_password(length)
    print(f"Your randomly generated password is: {password}")


if __name__ == "__main__":
    main()
