import sqlite3

if __name__ == "__main__":
    # Conectar ao banco de dados (ou criar um novo arquivo de banco de dados local)
    conn = sqlite3.connect('src/farmtech.db')
    cursor = conn.cursor()

    # Criar a tabela Tipo_Sensor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tipo_Sensor (
        id_tipo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT
    );
    ''')

    # Criar a tabela Sensor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sensor (
        id_sensor INTEGER PRIMARY KEY AUTOINCREMENT,
        id_tipo INTEGER,
        nome_sensor TEXT NOT NULL,
        localizacao TEXT,
        FOREIGN KEY (id_tipo) REFERENCES Tipo_Sensor(id_tipo)
    );
    ''')

    # Criar a tabela Medicao_Sensor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Medicao_Sensor (
        id_medicao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sensor INTEGER,
        valor REAL,
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_sensor) REFERENCES Sensor(id_sensor)
    );
    ''')

    # Criar a tabela Status_Rele
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Status_Rele (
        id_status INTEGER PRIMARY KEY AUTOINCREMENT,
        estado BOOLEAN NOT NULL,  -- true para ligado, false para desligado
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # Inserir dados iniciais na tabela Tipo_Sensor
    cursor.executemany('''
    INSERT INTO Tipo_Sensor (nome, descricao)
    VALUES (?, ?)
    ''', [
        ('K', 'Sensor para medir o nível de Potássio'),
        ('P', 'Sensor para medir o nível de Fósforo'),
        ('pH', 'Sensor para medir o nível de pH do solo'),
        ('Umidade', 'Sensor para medir a umidade do solo')
    ])

    # Inserir sensores iniciais na tabela Sensor
    cursor.executemany('''
    INSERT INTO Sensor (id_tipo, nome_sensor, localizacao)
    VALUES (?, ?, ?)
    ''', [
        (1, 'Sensor K', 'Setor A'),
        (2, 'Sensor P', 'Setor A'),
        (3, 'Sensor pH', 'Setor A'),
        (4, 'Sensor Umidade', 'Setor A')
    ])

    # Salvar as alterações e fechar a conexão
    conn.commit()
    conn.close()

    print("Banco de dados e tabelas criados com sucesso no arquivo farmtech.db")
