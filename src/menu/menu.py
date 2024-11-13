from src.db.db import get_sensores, get_tipos_sensores

def print_tipos_sensores():
    tipos = get_tipos_sensores()
    print("\nTypes of sensors:")
    for tipo in tipos:
        print(tipo)

def print_sensores():
    sensores = get_sensores()
    print("\nSensors:")
    for sensor in sensores:
        print(sensor)


menu_options = {
    1: {"display_text": "List available sensor types", "function": print_tipos_sensores},
    2: {"display_text": "List available sensors", "function": print_sensores},
    9: {"display_text": "Exit", "function": lambda: print("Exiting...")}
}


def print_menu():
    print("\nMenu:")
    for key in menu_options.keys():
        print(f"{key}: {menu_options[key]['display_text']}")


def run_menu():
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in menu_options:
                if choice == 9:
                    print("\nOption selected: ", choice, ": ", menu_options[choice]["display_text"])
                    menu_options[choice]["function"]()
                    break
                print("\nOption selected: ", choice, ": ", menu_options[choice]["display_text"])
                menu_options[choice]["function"]()
            else:
                print("\nInvalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    run_menu()
