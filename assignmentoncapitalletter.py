def is_proper_name(name):
    # Check if the first character is uppercase and the rest are lowercase
    return name[0].isupper() and name[1:].islower()

def main():    
    name = input("Enter a name: ")
    
    # Check if the name is properly capitalized
    if is_proper_name(name):
        print(f"The name '{name}' is properly capitalized.")
    else:
        print(f"The name '{name}' is not properly capitalized.")
if __name__ == "__main__":
    main()