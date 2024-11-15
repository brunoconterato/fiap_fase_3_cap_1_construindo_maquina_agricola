# Documentação do Projeto: Sistema de Irrigação Automatizado

## Visão Geral

Este projeto consiste em um sistema automatizado de monitoramento e controle de irrigação para plantações. O sistema utiliza sensores para medir parâmetros ambientais, como umidade do solo, pH e níveis de nutrientes (Potássio e Fósforo). Com base nesses dados, o sistema decide automaticamente quando acionar a irrigação, otimizando o uso da água e promovendo práticas agrícolas mais eficientes.

## Funcionalidades

- **Monitoramento em Tempo Real**: Leitura contínua de dados de sensores de umidade, pH e nutrientes do solo.
- **Automação da Irrigação**: Acionamento automático da bomba d'água com base em critérios definidos.
- **Armazenamento de Dados**: Registro de medições e status da bomba em um banco de dados SQLite para análise posterior.
- **Interface de Menu**: Permite configurações e ajustes manuais no sistema de irrigação.

## Descrição Detalhada dos Sensores

### Sensor DHT22 (Umidade do Solo)

- **Função**: O DHT22 é um sensor de temperatura e umidade digital que proporciona leituras de alta precisão. No projeto, é utilizado para medir a umidade relativa do solo, indicando a necessidade de irrigação.
- **Especificações**:
  - **Faixa de umidade**: 0% a 100% UR
  - **Precisão de umidade**: ±2% UR
  - **Tensão de operação**: 3.3V a 6V
  - **Tempo de resposta**: 2 segundos
- **Conexões**:
  - **VCC**: Conectado ao pino de **3.3V** do ESP32
  - **GND**: Conectado ao **GND** do ESP32
  - **Data**: Conectado ao pino **GPIO 17** do ESP32
- **Leitura dos Dados**:
  - A função `read_dht()` é responsável por ler a umidade do solo a partir do sensor DHT22.
  - Em caso de erro na leitura, uma mensagem de erro é exibida no monitor serial.
- **Referência**:
  - [Datasheet do DHT22](https://cdn-shop.adafruit.com/datasheets/DHT22.pdf)

### LDR (Fotoresistor) (Simulação do pH do Solo)

- **Função**: O LDR é utilizado para simular a medição do pH do solo, onde a intensidade luminosa captada pelo fotoresistor representa diferentes níveis de pH.
- **Especificações**:
  - **Sensibilidade à luz**: Alta sensibilidade a variações de luminosidade
  - **Tensão de operação**: 3.3V a 5V
- **Conexões**:
  - **VCC**: Conectado ao pino de **5V** do ESP32
  - **GND**: Conectado ao **GND** do ESP32
  - **Saída Analógica (AO)**: Conectado ao pino **GPIO 35** (entrada analógica) do ESP32
- **Leitura dos Dados**:
  - A função `read_ldr()` realiza a leitura do valor analógico fornecido pelo LDR.
  - O valor é convertido em resistência e posteriormente em lux, simulando o pH.
  - Uma relação entre a intensidade luminosa e o pH é estabelecida para simular as condições do solo.
- **Referência**:
  - [Tutorial sobre LDR com Arduino](https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogInput)

### Botão Verde (Simulação de Fósforo)

- **Função**: Simula a presença ou ausência de Fósforo (P) no solo. Quando pressionado, indica que há deficiência de Fósforo.
- **Conexões**:
  - **Terminal 1**: Conectado ao pino **GPIO 26** do ESP32
  - **Terminal 2**: Conectado ao **GND** do ESP32
- **Leitura dos Dados**:
  - O estado do botão é lido no `loop()` principal.
  - Se o botão estiver pressionado, a variável `P_buttonState` é definida como `LOW`, indicando deficiência de Fósforo.

### Botão Azul (Simulação de Potássio)

- **Função**: Simula a presença ou ausência de Potássio (K) no solo. Quando pressionado, indica que há deficiência de Potássio.
- **Conexões**:
  - **Terminal 1**: Conectado ao pino **GPIO 22** do ESP32
  - **Terminal 2**: Conectado ao **GND** do ESP32
- **Leitura dos Dados**:
  - O estado do botão é lido no `loop()` principal.
  - Se o botão estiver pressionado, a variável `K_buttonState` é definida como `LOW`, indicando deficiência de Potássio.

### Módulo Relé (Controle da Bomba d'Água)

- **Função**: Controla o acionamento da bomba d'água para irrigação, permitindo ligar ou desligar o fluxo de água conforme necessidade.
- **Especificações**:
  - **Tipo**: Relé de acionamento por sinal lógico
  - **Tensão de operação**: 5V (lado do relé), compatível com sinal de 3.3V do ESP32
- **Conexões**:
  - **VCC**: Conectado ao pino de **5V** do ESP32
  - **GND**: Conectado ao **GND** do ESP32
  - **IN (Controle)**: Conectado ao pino **GPIO 21** do ESP32
- **Controle**:
  - A função `liga_rele()` ativa o relé, ligando a bomba d'água.
  - A função `desliga_rele()` desativa o relé, desligando a bomba.
- **Considerações**:
  - É importante garantir que o relé seja compatível com os níveis lógicos do ESP32 ou utilizar um transistor para adaptar o sinal.

## Fluxo de Informação e Lógica de Irrigação

A lógica de irrigação está detalhadamente explicada no documento [Lógica de Irrigação](./document/other/irrigation_logic.md). O fluxo geral é:

1. **Leitura dos Sensores**:
   - A cada iteração do `loop()`, o sistema lê os valores dos sensores de umidade, pH, Potássio e Fósforo.
2. **Análise das Condições**:
   - A função `deveIrrigar()` avalia se a irrigação é necessária com base nos valores obtidos.
3. **Acionamento da Irrigação**:
   - Se a irrigação for necessária, `liga_rele()` é chamada para ligar a bomba.
   - Caso contrário, `desliga_rele()` é chamada para desligar a bomba.
4. **Registro dos Dados**:
   - Os dados das medições e o estado da bomba são registrados no banco de dados, conforme descrito em [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados).

Para entender a implementação detalhada da função `deveIrrigar()` e a lógica aplicada, consulte o documento [Lógica de Irrigação](./document/other/irrigation_logic.md).

## Diagrama de Conexões

O diagrama completo das conexões dos sensores e módulos está disponível em [Diagrama dos Sensores](./document/other/sensor_diagram.md).

**Resumo das Conexões**:

- **ESP32**:
  - **GPIO 17**: Sensor DHT22 (Umidade)
  - **GPIO 35**: LDR (Simulação de pH)
  - **GPIO 26**: Botão Verde (Fósforo)
  - **GPIO 22**: Botão Azul (Potássio)
  - **GPIO 21**: Módulo Relé (Bomba d'água)

## Componentes de Hardware

- **Microcontrolador ESP32**: Placa de desenvolvimento utilizada para controlar todo o sistema.
- **Sensor DHT22**: Sensor digital de umidade e temperatura.
- **LDR (Fotoresistor)**: Sensor analógico que varia a resistência conforme a intensidade luminosa.
- **Botões Push-button**: Utilizados para simular a ausência de nutrientes no solo.
- **Módulo Relé**: Permite o controle de dispositivos de alta tensão/corrente como a bomba d'água.

## Componentes de Software

- **Código em C++ (`sketch.ino`)**:
  - Implementa a lógica de controle no ESP32.
  - Inclui funções para leitura dos sensores, lógica de decisão e controle do relé.
  - Para detalhes do código, consulte o projeto no [Wokwi](https://wokwi.com/projects/414492759278919681).
- **Scripts em Python**:
  - **`initialize_db.py`**: Inicializa o banco de dados SQLite e cria as tabelas necessárias.
  - **`db.py`**: Contém funções para inserir e recuperar dados do banco de dados.
  - **`menu.py`**: Implementa uma interface de menu para interagir com o sistema.
- **Banco de Dados SQLite**:
  - Armazena as medições dos sensores e o status da bomba.
  - A estrutura do banco de dados está descrita na seção [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados).

## Estrutura do Banco de Dados

As tabelas criadas e suas descrições estão detalhadas no documento [AI Project Document](./document/ai_project_document_fiap.md#anexo-1-estrutura-do-banco-de-dados). Principais tabelas:

- **Tipo_Sensor**: Contém os tipos de sensores (K, P, pH, Umidade).
- **Sensor**: Armazena informações sobre cada sensor e sua localização.
- **Medicao_Sensor**: Registra as medições dos sensores com timestamp.
- **Rele**: Armazena informações sobre os relés utilizados.
- **Status_Rele**: Registra o estado do relé (ligado/desligado) ao longo do tempo.

## Configuração do Ambiente e Execução

Para executar o projeto, siga as instruções detalhadas no [README.md](./README.md), seção **Como executar o código**.

Resumidamente:

1. **Configurar o Ambiente Python**:
   - Criar e ativar um ambiente virtual.
   - Instalar as dependências com `pip install -r requirements.txt`.
2. **Inicializar o Banco de Dados**:
   - Executar `python3 scripts/initialize_db.py` para criar o banco de dados e as tabelas.
3. **Carregar o Código no ESP32**:
   - Abrir `sketch.ino` no Arduino IDE ou Wokwi.
   - Verificar se as bibliotecas necessárias estão instaladas.
   - Fazer o upload do código para o ESP32.
4. **Execução do Sistema**:
   - O sistema iniciará automaticamente a leitura dos sensores e controle da irrigação.
   - Dados serão registrados no banco de dados para análise posterior.

## Vídeo de demonstração

Um vídeo demonstrativo do sistema em funcionamento está disponível em [Vídeo de Demonstração](https://youtu.be/xFps6HnP7jE).

## Conclusão

Este projeto demonstra a implementação de um sistema de irrigação automatizado, combinando sensores, controle eletrônico e armazenamento de dados. A solução visa otimizar o uso de recursos hídricos na agricultura, promovendo práticas sustentáveis e aumentando a eficiência produtiva.