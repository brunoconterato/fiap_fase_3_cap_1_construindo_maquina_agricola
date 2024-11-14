# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Sistema de Irrigação Automatizado

## Sobre o grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/brunoconterato">Bruno Conterato</a> 
- <a href="https://www.linkedin.com/in/willianpmarques">Willian Pinheiro Marques</a> 
- <a href="https://www.linkedin.com/in/robertobesser">Roberto Besser</a>
- <a href="https://www.linkedin.com/in/ludimila-vi">Ludimila Vitorino</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>


## 📜 Descrição

Este projeto consiste em um sistema automatizado de monitoramento e controle de irrigação de plantações. Desenvolvido para facilitar o gerenciamento de grandes áreas agrícolas, o sistema utiliza sensores para medir parâmetros ambientais como umidade do solo e temperatura, ajustando automaticamente a irrigação conforme as necessidades da plantação. Inicialmente, o sistema eletrônico foi desenvolvido em **MicroPython** para rápida prototipagem, sendo posteriormente traduzido para **C++** para otimizar desempenho. Na versão final, implementada em um microcontrolador simulado no Wokwi, o sistema combina sensores de umidade, relés para ativar/desativar bombas de água, e uma interface de menu para configurações manuais.

O projeto foi desenvolvido ao longo de várias fases, cada uma agregando novas funcionalidades e refinando o sistema. O código é modular, com cada função encapsulada em arquivos específicos. A automação permite reduzir o desperdício de água e otimizar o crescimento das culturas, contribuindo para práticas agrícolas mais sustentáveis e eficientes.


Para mais informações, acesse:
- [Documentação do projeto](./document/ai_project_document_fiap.md)
- [Lógica de irrigação](./document/other/irrigation_logic.md)
- [Diagrama de conexão dos sensores](./document/other/sensor_diagram.md)
- [Código-fonte no Wokwi](https://wokwi.com/projects/414146597880886273)

---

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **.github**: Pasta que poderá ser usada para arquivos de configuração específicos do GitHub, como workflows e ações, para automatizar processos no repositório.

- **assets**: Contém elementos visuais e não-estruturados do repositório. Por exemplo, `logo-fiap.png`, a imagem que representa a marca do projeto.

- **config**: Local onde podem ser posicionados arquivos de configuração específicos do projeto, como variáveis de ambiente, mas atualmente não está presente na estrutura fornecida.

- **document**: Armazena a documentação detalhada do projeto. O arquivo principal é o `ai_project_document_fiap.md`, que descreve as funcionalidades e arquitetura do sistema. Na subpasta **other**, há documentos adicionais, como `irrigation_logic.md`, que explica a lógica de irrigação implementada.

- **scripts**: Inclui scripts auxiliares para tarefas específicas, como `initialize_db.py`, que configura o banco de dados inicial do projeto, facilitando o deploy e testes de ambiente.

- **src**: Contém todo o código fonte do projeto, organizado em subpastas para facilitar a navegação. Principais subpastas e arquivos:
  - **db**: Inclui `db.py`, que lida com as operações e conexões com o banco de dados.
  - **farmtech.db**: Banco de dados SQLite que armazena as informações persistentes do sistema, como dados de sensores e registros de irrigação.
  - **main.py**: Script principal que inicializa o sistema e orquestra as operações do projeto.
  - **menu**: Inclui `menu.py`, que implementa a interface de menu do usuário, permitindo configurações e ajustes no sistema de irrigação.
  - **Wokwi**: Contém arquivos para simulação no ambiente Wokwi:
    - `diagram.json`: Diagrama que modela o circuito eletrônico.
    - `libraries.txt`: Dependências de bibliotecas usadas no código.
    - `sketch.ino`: Código final em C++ para controle dos sensores e relés.
    - `wokwi-project.txt`: Descrição e metadados do projeto no Wokwi.

- **README.md**: Documento atual que serve como guia e explicação geral sobre o projeto, facilitando a compreensão e navegação da estrutura.

## 🔧 Como executar o código

### Configurando o Ambiente Virtual Python

Siga estes passos para criar e usar um ambiente virtual para este projeto.

#### 1. Crie o Ambiente Virtual
Execute este comando para criar um ambiente virtual em uma pasta chamada `venv`:

```bash
python3 -m venv venv
```

#### 2. Ative o Ambiente Virtual
- **Linux / MacOS**: 
  ```bash
  source venv/bin/activate
  ```

- **Windows**: 
  ```cmd
  venv\Scripts\activate
  ```

Quando ativado, seu terminal mostrará `(venv)` no início do prompt.

#### 3. Instale as Dependências
Uma vez que o ambiente esteja ativo, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```
#### 4. Desative o Ambiente Virtual
Para parar de usar o ambiente virtual, desative-o executando:

```bash
deactivate
```

---

#### Notas Adicionais

- **Salvar Novas Dependências**: Após instalar novos pacotes, salve-os em `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```

### Instruções de Configuração do Projeto

Para executar a configuração inicial e inicializar o banco de dados para este projeto, siga a instrução abaixo:

#### Execute o Script de Inicialização do Banco de Dados

Navegue até a pasta do projeto e execute o seguinte comando para rodar o script de inicialização do banco de dados, que configurará o ambiente e criará os bancos de dados necessários:

```bash
python3 scripts/initialize_db.py
```

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>