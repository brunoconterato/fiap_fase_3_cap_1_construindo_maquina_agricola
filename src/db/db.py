import sqlite3
from datetime import datetime
import os

DB_PATH = "src/farmtech.db"


def get_tipos_sensores():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Tipo_Sensor")
        return cursor.fetchall()


def get_sensores():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sensor")
        return cursor.fetchall()
    
    
def get_medicoes():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medicao_Sensor")
        return cursor.fetchall()


def insert_medicao_sensor(id_sensor, valor):
    # Check id_sensor exists
    sensors = get_sensores()
    sensor_ids = [sensor[0] for sensor in sensors]
    if id_sensor not in sensor_ids:
        raise ValueError("Sensor ID not found.")

    # Insert data into Medicao_Sensor
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Medicao_Sensor (id_sensor, valor, data_hora)
            VALUES (?, ?, ?)
            """,
            (id_sensor, valor, datetime.now()),
        )
        conn.commit()

def get_status_rele():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Status_Rele")
        return cursor.fetchall()
    
def insert_status_rele(estado):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Status_Rele (estado, data_hora)
            VALUES (?, ?)
            """,
            (estado, datetime.now()),
        )
        conn.commit()