def add_integers(first_value, second_value):
    if type(first_value) is not type(second_value):
        raise TypeError("Both parameters must be of the same data type.")
    return first_value + second_value

def main():
    first_input = input("Enter the first integer: ")
    second_input = input("Enter the second integer: ")

    try:
        first_number = int(first_input)
        second_number = int(second_input)
        result = add_integers(first_number, second_number)
    except ValueError:
        print("Please enter valid integers only.")
        return
    except TypeError as error:
        print(error)
        return

    print(f"Sum: {result}")


if __name__ == "__main__":
    main()
