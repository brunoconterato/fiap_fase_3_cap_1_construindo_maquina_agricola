from typing import Callable, TypedDict, Dict
from src.db.db import (
    get_medicoes,
    get_relays,
    get_sensores,
    get_status_rele,
    get_tipos_sensores,
    insert_medicao_sensor,
    insert_status_rele,
)
import pandas as pd


def print_tipos_sensores():
    tipos = get_tipos_sensores()
    tipos_df = pd.DataFrame(tipos, columns=["id_tipo", "nome", "descricao"])
    print("\nTypes of sensors:")
    print(tipos_df.to_string(index=False))


def print_sensores():
    sensores = get_sensores()
    sensores_df = pd.DataFrame(
        sensores, columns=["id_sensor", "id_tipo", "nome_sensor", "localizacao"]
    )
    print("\nSensors:")
    print(sensores_df.to_string(index=False))


def print_medicoes():
    medicoes = get_medicoes()
    medicoes_df = pd.DataFrame(
        medicoes, columns=["id_medicao", "id_sensor", "valor", "data_hora"]
    )
    print("\nMeasures data:")
    print(medicoes_df.to_string(index=False))

def print_relays():
    relays = get_relays()
    relays_df = pd.DataFrame(
        relays, columns=["id_rele", "nome_rele", "localizacao"]
    )
    print("\nRelays:")
    print(relays_df.to_string(index=False))

# Function to add data to Medicao_Sensor
def add_medicao_sensor():
    try:
        # List available sensors for reference
        print("Available sensors:")
        print_sensores()
        
        sensors = get_sensores()

        # Get user input for sensor data
        while True:
            id_sensor = int(input("\nEnter the sensor ID: "))
            if id_sensor in [sensor[0] for sensor in sensors]:
                break
            else:
                print("Invalid sensor ID. Please enter a valid sensor ID from the list.")
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
    status_df = pd.DataFrame(status, columns=["id_status", "id_rele", "estado", "data_hora"])
    print("\nRelay status:")
    print(status_df.to_string(index=False))

def add_status_rele():
    try:
        # Get user input for relay status
        relays = get_relays()
        print("Available relays:")
        print_relays()
        
        while True:
            relay_id = int(input("\nEnter the relay ID: "))
            if relay_id in [relay[0] for relay in relays]:
                break
            else:
                print("Invalid relay ID. Please enter a valid relay ID from the list.")
            
        # Validate relay status input
        while True:
            estado_input = input("\nEnter the relay status (0 or 1): ")
            if estado_input in ["0", "1"]:
                estado = bool(int(estado_input))
                break
            else:
                print("Invalid input. Please enter 0 or 1.")

        # Insert data into Status_Rele
        try:
            insert_status_rele(relay_id, estado)
            print("Relay status added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def show_statistics():
    # Get sensor data
    medicoes = get_medicoes()
    medicoes_df = pd.DataFrame(
        medicoes, columns=["id_medicao", "id_sensor", "valor", "data_hora"]
    )

    # Get relay status
    status = get_status_rele()
    status_df = pd.DataFrame(status, columns=["id_status", "id_rele", "estado", "data_hora"])

    # Print statistics of measures grouped by sensor, only for "valor" column
    print("\nSensor values statistics:")
    print(medicoes_df.groupby("id_sensor")["valor"].describe())

    # Print statistics of relay status by relay
    print("\nRelay status:")
    print(status_df.groupby("id_rele")["estado"].describe())
    
    # Print the number os states for relay status
    print("\nCount relay status:")
    print(status_df.groupby("id_rele")["estado"].value_counts())


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
    3: {"display_text": "List available relays", "function": print_relays},
    4: {"display_text": "List sensor data", "function": print_medicoes},
    5: {"display_text": "List relay status", "function": print_relay_status},
    6: {
        "display_text": "Enter sensor data",
        "function": add_medicao_sensor,
    },
    7: {"display_text": "Enter relay status", "function": add_status_rele},
    8: {"display_text": "Show statistics", "function": show_statistics},
    9: {"display_text": "Exit", "function": lambda: print("Exiting...")},
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
