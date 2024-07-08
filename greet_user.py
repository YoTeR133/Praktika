def greet_user():
    name = input("Введите ваше имя: ")
    if name:
        print(f"Привет, {name}!")
    else:
        print("Вы не ввели имя.")

def farewell_user():
    print("До свидания!")

if __name__ == "__main__":
    greet_user()
    farewell_user()