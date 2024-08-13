# greeting.py

def greet(name):
    """Function to print a greeting message."""
    print(f"Hello, {name}! Welcome to Python programming.")

def main():
    """Main function to execute the program."""
    name = input("Enter your name: ")
    greet(name)

if __name__ == "__main__":
    main()
