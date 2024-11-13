from src.menu.menu import run_menu
from src.db.db import get_sensores, get_tipos_sensores


def main():
    # Consultar tipos de sensores
    tipos = get_tipos_sensores()
    print("Tipos de Sensores:")
    for tipo in tipos:
        print(tipo)

    # Consultar sensores
    sensores = get_sensores()
    print("\nSensores:")
    for sensor in sensores:
        print(sensor)

if __name__ == "__main__":
    run_menu()
