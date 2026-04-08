def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

def add_integers(first_value, second_value):
    if type(first_value) is not type(second_value):
        raise TypeError("Both parameters must be of the same data type.")

    if type(first_value) is not int:
        raise TypeError("Both parameters must be integers.")

    return first_value + second_value


def main():
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        return

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


if __name__ == "__main__":
    main()
