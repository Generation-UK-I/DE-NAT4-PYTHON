# Data Persistence Sample App



```py
import datetime

diary_FILE = "my_diary.txt"

def show_menu():
    """Display the menu options"""
    print("\n=== MY diary ===")
    print("1. Write a new entry")
    print("2. Read all entries")
    print("3. Exit")
    print("=" * 17)

def write_entry():
    """Write a new diary entry"""
    print("\n--- New Entry ---")
    entry_text = input("What happened today? ")
    
    # Add timestamp
    timestamp = datetime.datetime.now()
    
    # Write to file (append mode)
    with open(diary_FILE, "a") as file:
        file.write(f"\n[{timestamp}]\n")
        file.write(f"{entry_text}\n")
        file.write("-" * 30 + "\n")
    
    print("✓ Entry saved!")

def read_entries():
    """Read all diary entries"""
    print("\n--- Your diary ---")
    
    try:
        with open(diary_FILE, "r") as file:
            content = file.read()
        
        if content.strip() == "":
            print("Your diary is empty. Write an entry first!")
        else:
            print(content)
            
    except FileNotFoundError:
        print("No diary yet. Write your first entry!")

def main():
    """Main program"""
    print("Welcome to your diary!")
    
    while True:
        show_menu()
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("\nGoodbye! Your entries are saved.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

main()
```