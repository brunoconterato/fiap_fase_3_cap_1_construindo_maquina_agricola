
<img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=30% height=30%>

# AI Project Document - Módulo 1 - FIAP

**_Os trechos em itálico servem apenas como guia para o preenchimento da seção. Por esse motivo, não devem fazer parte da documentação final_**

## Nome do Grupo

#### Nomes dos integrantes do grupo

## Sumário
1. Introdução
2. Visão Geral do Projeto
3. Desenvolvimento do Projeto
4. Resultados e Avaliações
5. Conclusões e Trabalhos Futuros
6. Referências
7. Anexos

## 1. Introdução

### 1.1. Escopo do Projeto

#### 1.1.1. Contexto da Inteligência Artificial
Este projeto faz parte de um sistema de Agricultura de Precisão, com foco na automação de um sistema de irrigação inteligente. A Inteligência Artificial e IoT aplicadas ao setor agrícola permitem que produtores maximizem o uso de recursos, como água e nutrientes, promovendo uma prática agrícola mais sustentável e econômica.

#### 1.1.2. Descrição da Solução Desenvolvida
A solução desenvolvida é um sistema de irrigação automatizado que utiliza sensores para monitoramento em tempo real de parâmetros de solo, como umidade, pH e níveis de nutrientes (P e K). Com isso, a bomba d’água é acionada automaticamente com base nas condições do solo. Além disso, o sistema realiza armazenamento em um banco de dados, facilitando o acompanhamento histórico e a análise de dados do solo.

## 2. Visão Geral do Projeto

### 2.1. Objetivos do Projeto
O objetivo principal é desenvolver um sistema que:
1. Monitore em tempo real os dados de umidade, nutrientes e pH do solo.
2. Controle automaticamente uma bomba d’água com base nesses dados.
3. Armazene os dados coletados em um banco de dados SQL.

### 2.2. Público-Alvo
O sistema é voltado para agricultores e empresas agrícolas que buscam otimizar o uso de recursos hídricos e maximizar a produtividade, especialmente em regiões onde o acesso à água é limitado.

### 2.3. Metodologia
Para o desenvolvimento do projeto, foi adotada uma metodologia baseada nas seguintes etapas:
1. Levantamento dos requisitos.
2. Desenvolvimento e teste do sistema de sensores com o ESP32.
3. Implementação das funcionalidades de CRUD no banco de dados SQL.
4. Testes e ajustes no controle automatizado da irrigação com o relé.
5. Documentação e criação do repositório no GitHub.

## 3. Desenvolvimento do Projeto

### 3.1. Tecnologias Utilizadas
- **Hardware**: ESP32, sensor DHT22, botões simulando sensores de nutrientes, LDR (sensor de luz).
- **Software**: Arduino (IDE), Python (CRUD no banco de dados), SQLite.
- **Bibliotecas**: DHT para sensor DHT22, biblioteca `sqlite3` para Python.
- **Simulador**: Wokwi para o circuito eletrônico.

### 3.2. Modelagem e Algoritmos
- **Algoritmo de Decisão de Irrigação**: A função `deveIrrigar` toma a decisão com base nos valores dos sensores e nos parâmetros definidos para umidade, pH e nutrientes. Este modelo básico considera irrigação sempre que a umidade estiver abaixo de 30%, o pH fora do intervalo de 5.5 a 7.5, ou a presença de deficiência em K ou P.
- **CRUD no Banco de Dados**: O sistema implementa operações de consulta e inserção de leituras de sensores e status da bomba d’água. Foi criada uma estrutura de tabelas para organizar os dados dos sensores, medições e status do relé.

### 3.3. Treinamento e Teste
Não há modelo de IA para treinamento, pois o sistema opera com lógica de regras para tomada de decisão de irrigação. Testes manuais foram realizados no simulador Wokwi, e dados foram coletados para armazenar no banco de dados.

### 3.4 Evolução do Sistema Eletrônico

Inicialmente, o sistema eletrônico foi desenvolvido em **MicroPython** para facilitar a prototipagem e a validação dos sensores e dos controles do relé. Essa versão inicial foi implementada e testada no [Wokwi](https://wokwi.com/projects/412840257175989249) e permitiu ajustes rápidos no código e nos componentes antes de avançar para uma implementação mais robusta.

Após os testes bem-sucedidos na versão MicroPython, o sistema foi traduzido para **C++** ([versão final no Wokwi](https://wokwi.com/projects/414104064226887681)), que oferece maior desempenho e flexibilidade para controle do hardware em nível mais baixo. A versão final em C++ incluiu ajustes adicionais para otimizar o funcionamento do relé e a integração com os sensores, garantindo a confiabilidade do sistema.

## 4. Resultados e Avaliações

### 4.1. Análise dos Resultados
Os testes demonstraram que o sistema é capaz de acionar a bomba automaticamente em resposta aos níveis de umidade, pH e nutrientes, conforme esperado. Houve desafios com precisão dos sensores no simulador e na integração de dados em tempo real no banco de dados.

### 4.2. Feedback dos Usuários
Os testes foram realizados exclusivamente no simulador Wokwi, sem a inclusão de feedback humano. O simulador permitiu verificar o funcionamento do sistema de irrigação automatizado, mas não forneceu insights sobre a experiência do usuário final ou sugestões de melhorias na interface de monitoramento.

## 5. Conclusões e Trabalhos Futuros

A solução desenvolvida atingiu o objetivo principal de automatizar a irrigação com base nas condições do solo. No futuro, o sistema pode ser expandido para incluir:
1. Um painel de controle para monitoramento em tempo real e ajuste de parâmetros.
2. Integração com APIs meteorológicas para otimizar a irrigação.
3. Aplicação de algoritmos de aprendizado de máquina para análise de padrões de solo.

## 6. Referências
- Datasheets dos sensores DHT22 e ESP32.
- Documentação da biblioteca `sqlite3` em Python.
- Exemplos de projetos similares de agricultura de precisão e irrigação inteligente.

## Anexos

### Anexo 1: Estrutura do Banco de Dados

- **Tipo_Sensor**: Tabela que contém informações sobre o tipo de sensor (K, P, pH, Umidade).
- **Sensor**: Tabela que armazena cada sensor e sua localização.
- **Medicao_Sensor**: Tabela com as medições registradas pelos sensores.
- **Status_Rele**: Tabela com o estado da bomba d’água (ligado/desligado) ao longo do tempo.

### Anexo 2: Código Fonte

- **Script de Inicialização do Banco de Dados (SQLite)**: Ver seção do script para criação e inserção inicial de dados.
- **Código do ESP32 (Wokwi)**: Código C++ para controle do ESP32 com sensores.
- **Funções de CRUD em Python**: Ver seção das funções `insert_medicao_sensor` e `insert_status_rele`.
