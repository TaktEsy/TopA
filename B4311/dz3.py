import random

def get_user_choice():
    print("Выберите: камень, ножницы или бумага")
    while True:
        user_input = input("Ваш выбор: ").strip().lower()
        if user_input in ["камень", "ножницы", "бумага"]:
            return user_input
        print("Неверный ввод. Попробуйте снова.")

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень")
    ):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_game():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

        play_again = input("Хотите сыграть снова? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру! До встречи!")
            break

if __name__ == "__main__":
    play_game()
