import sqlite3

def get_tipos_sensores(cursor):
    cursor.execute("SELECT * FROM Tipo_Sensor")
    return cursor.fetchall()

def get_sensores(cursor):
    cursor.execute("SELECT * FROM Sensor")
    return cursor.fetchall()

def main():
    # Conectar ao banco de dados
    with sqlite3.connect('src/farmtech.db') as conn:
        cursor = conn.cursor()

        # Consultar tipos de sensores
        tipos = get_tipos_sensores(cursor)
        print("Tipos de Sensores:")
        for tipo in tipos:
            print(tipo)

        # Consultar sensores
        sensores = get_sensores(cursor)
        print("\nSensores:")
        for sensor in sensores:
            print(sensor)

if __name__ == "__main__":
    main()
