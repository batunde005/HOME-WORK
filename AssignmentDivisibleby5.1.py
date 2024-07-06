def is_a_number_divisible_by_5_1(number):
    # Check if the number is divisible by 5.1
    return number % 5.1 == 0

def main():
    # Input number
    number = float(input("Enter a number: "))
    
    # Check if the number is divisible by 5.1
    if is_a_number_divisible_by_5_1(number):
        print(f"The number {number} is divisible by 5.1.")
    else:
        print(f"The number {number} is not divisible by 5.1.")

if __name__ == "__main__":
    main()