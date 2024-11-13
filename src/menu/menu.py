from typing import Callable, TypedDict, Dict
from src.db.db import get_medicoes, get_sensores, get_status_rele, get_tipos_sensores, insert_medicao_sensor, insert_status_rele


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
        
def print_medicoes():
    medicoes = get_medicoes()
    print("\nSensor data:")
    for medicao in medicoes:
        print(medicao)


# Function to add data to Medicao_Sensor
def add_medicao_sensor():
    try:
        # List available sensors for reference
        print("Available sensors:")
        print_sensores()

        # Get user input for sensor data
        id_sensor = int(input("\nEnter the sensor ID: "))
        valor = float(input("\nEnter the measurement value: "))

        # Insert data into Medicao_Sensor
        try:
            insert_medicao_sensor(id_sensor, valor)
            print("Measurement data added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def print_relay_status():
    status = get_status_rele()
    print("\nRelay status:")
    for s in status:
        print(s)

def add_status_rele():
    try:
        # Get user input for relay status
        estado = bool(input("\nEnter the relay status (0 or 1): "))

        # Insert data into Status_Rele
        try:
            insert_status_rele(estado)
            print("Relay status added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

class MenuItem(TypedDict):
    display_text: str
    function: Callable[[], None]


MenuOptions = Dict[int, MenuItem]

menu_options: MenuOptions = {
    1: {
        "display_text": "List available sensor types",
        "function": print_tipos_sensores,
    },
    2: {"display_text": "List available sensors", "function": print_sensores},
    3: {"display_text": "List sensor data", "function": print_medicoes},
    4: {
        "display_text": "Enter sensor data",
        "function": add_medicao_sensor,
    },
    5: {"display_text": "List relay status", "function": print_relay_status},
    6: {"display_text": "Enter relay status", "function": add_status_rele},
    7: {"display_text": "Exit", "function": lambda: print("Exiting...")},
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
                if choice == 7:
                    print(
                        "\nOption selected: ",
                        choice,
                        ": ",
                        menu_options[choice]["display_text"],
                    )
                    menu_options[choice]["function"]()
                    break
                print(
                    "\nOption selected: ",
                    choice,
                    ": ",
                    menu_options[choice]["display_text"],
                )
                menu_options[choice]["function"]()
            else:
                print("\nInvalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    run_menu()
