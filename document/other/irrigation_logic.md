# Documentação do Sistema de Irrigação Inteligente - Lógica de Irrigação

## Visão Geral
O sistema de irrigação inteligente foi desenvolvido para monitorar e ajustar o nível de umidade do solo em uma área agrícola, utilizando parâmetros de nutrientes (K e P) e pH do solo. A lógica do sistema baseia-se em dados de sensores e toma decisões automáticas sobre quando ligar ou desligar a bomba d’água, promovendo o uso eficiente de recursos hídricos e otimizando a absorção de nutrientes pela cultura.

## Lógica de Irrigação
### Condições de Ativação e Desativação da Bomba
A bomba de irrigação é acionada automaticamente com base em três parâmetros principais:
1. **Umidade do Solo:** Verificada através de um sensor DHT22.
2. **Níveis de Nutrientes (Potássio e Fósforo):** Simulados através de botões.
3. **pH do Solo:** Simulado por um sensor de intensidade de luz (LDR).

A lógica de irrigação é implementada na função `deveIrrigar`, que verifica os seguintes critérios para decidir se a bomba deve ser ligada ou desligada:

- **Baixa Umidade do Solo:** Se a umidade estiver abaixo do limite (30%), a irrigação é recomendada imediatamente, independentemente dos demais parâmetros.
- **Níveis de Nutrientes:** Se os sensores de nutrientes (K e P) estiverem baixos, a irrigação é ativada para ajudar na absorção dos nutrientes pelo solo.
- **pH do Solo fora do Intervalo Ideal:** O sistema verifica se o pH está dentro do intervalo ideal de 5.5 a 7.5. Caso contrário, a irrigação é ativada para auxiliar na correção do pH.

### Função `deveIrrigar`
A função `deveIrrigar` implementa a lógica de decisão para irrigação com base nos critérios mencionados:

```cpp
bool deveIrrigar(bool K, bool P, float pH, float humidity) {
  // Limites para pH e umidade
  float pH_min = 5.5;  // pH mínimo aceitável para o solo
  float pH_max = 7.5;  // pH máximo aceitável para o solo
  float humidity_threshold = 30.0;  // Umidade mínima aceitável (em %)

  if (humidity < humidity_threshold) {
    Serial.println("Irrigação recomendada. Motivo: baixa umidade.");
    return true;
  }

  if (!K || !P) {
    Serial.println("Irrigação recomendada. Motivo: baixo nível de K ou P.");
    return true;
  }

  if (pH < pH_min || pH > pH_max) {
    Serial.println("Irrigação recomendada. Motivo: pH fora da faixa recomendada.");
    return true;
  }

  Serial.println("Irrigação não recomendada. Motivo: todos os parâmetros normais.");
  return false;
}
```

## Componentes Eletrônicos e Funções
### Microcontrolador ESP32
- **Descrição:** O ESP32 atua como controlador principal, responsável por coletar dados dos sensores e enviar comandos ao relé.
- **Funções Principais:** 
  - **`setup`:** Configura os pinos dos sensores e do relé.
  - **`loop`:** Executa a lógica de leitura de sensores e decide o acionamento da bomba.

### Sensores Utilizados
1. **Sensor de Umidade (DHT22):**
   - **Pino:** DHT_PIN (pino 17).
   - **Função de Leitura:** `read_dht`, que coleta o valor de umidade e exibe no monitor serial.

2. **Sensor de Nutrientes (K e P):**
   - **Pinos:** Botões em P_green_buttonPin (pino 26) e K_blue_buttonPin (pino 22).
   - **Função de Leitura:** Variáveis `P_buttonState` e `K_buttonState` verificam o estado dos botões para simular a presença de nutrientes.

3. **Sensor de pH (LDR):**
   - **Pino:** LDR_PIN (pino 35).
   - **Função de Leitura:** `read_ldr`, que calcula o valor de intensidade luminosa e simula a variação de pH do solo com base em resistência.

### Relé e Bomba d'Água
- **Pino:** RELE_PIN (pino 21).
- **Controle do Relé:** A função `liga_rele` aciona a bomba de água quando a irrigação é necessária, e a função `desliga_rele` a desativa.
  - **Funções:**
    - **`liga_rele`:** Ativa o relé e liga a bomba d'água, registrando no monitor serial.
    - **`desliga_rele`:** Desativa o relé e desliga a bomba, indicando o status no monitor serial.

## Fluxo de Decisão para Irrigação
A cada execução do `loop`, o sistema:
1. **Lê os Sensores:** Coleta dados dos sensores de nutrientes, umidade e pH.
2. **Avalia Condições de Irrigação:** Chama `deveIrrigar` para decidir se a irrigação é necessária.
3. **Controla o Relé:** Ativa ou desativa o relé conforme a necessidade de irrigação.

## Conclusão
A lógica implementada no sistema de irrigação inteligente proporciona um controle automatizado e eficiente, ajustando-se dinamicamente às condições do solo. Este controle melhora a eficiência hídrica e ajuda a garantir que o solo mantenha níveis ideais de umidade e nutrientes, contribuindo para a produtividade agrícola de maneira sustentável.
