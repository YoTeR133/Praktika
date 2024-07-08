def greet_user():
    name = input("Enter your name: ")
    if name:
        print(f"Hello, {name}!")
    else:
        print("You did not enter a name.")

def farewell_user():
    print("Goodbye!")

if __name__ == "__main__":
    greet_user()
    farewell_user()