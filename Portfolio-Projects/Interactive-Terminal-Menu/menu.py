# menu.py

def display_menu():
    """Display the main menu options."""
    print("\n=== Interactive Terminal Menu ===")
    print("1. View Current Date and Time")
    print("2. List Files in Current Directory")
    print("3. Generate a Random Number")
    print("4. Exit")

def view_date_time():
    """Display the current date and time."""
    from datetime import datetime
    print(f"\nCurrent Date and Time: {datetime.now()}")

def list_files():
    """List all files in the current directory."""
    import os
    files = os.listdir()
    print("\nFiles in Current Directory:")
    for file in files:
        print(f"- {file}")

def generate_random_number():
    """Generate and display a random number between 1 and 100."""
    import random
    random_number = random.randint(1, 100)
    print(f"\nRandom Number: {random_number}")

def main():
    """Run the interactive terminal menu."""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            view_date_time()
        elif choice == "2":
            list_files()
        elif choice == "3":
            generate_random_number()
        elif choice == "4":
            print("\nExiting the menu. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()