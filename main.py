def convert_number(number, base):
    if base == 2:
        return bin(number)[2:]
    elif base == 10:
        return str(number)
    elif base == 16:
        return hex(number)[2:]

def main():
    number = int(input("Enter a number: "))
    from_base = int(input("Enter the base of the number (2, 10, or 16): "))
    to_base = int(input("Enter the base you want to convert to (2, 10, or 16): "))
    if from_base not in [2, 10, 16] or to_base not in [2, 10, 16]:
        print("Invalid base entered. Please enter 2, 10, or 16.")
        return
    if from_base == to_base:
        print("The number in base", to_base, "is", convert_number(number, to_base))
    else:
        decimal_number = int(str(number), from_base)
        print("The number in base", to_base, "is", convert_number(decimal_number, to_base))

if __name__ == '__main__':
    main()
