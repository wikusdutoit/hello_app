import os

def main():
    if os.getenv('CI'):
        name = "GitHub Actions"
    else:
        name = input("Enter your name: ")
    print(f"Hello from the modify branch, {name}!")

if __name__ == "__main__":
    main()
