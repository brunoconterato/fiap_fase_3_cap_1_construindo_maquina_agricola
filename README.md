# fiap_fase_3_cap_1_construindo_maquina_agricola

# Setting Up the Python Virtual Environment

Follow these steps to create and use a virtual environment for this project.

### 1. Create the Virtual Environment
Run this command to create a virtual environment in a folder named `venv`:

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment
- **Linux / MacOS**: 
  ```bash
  source venv/bin/activate
  ```

- **Windows**: 
  ```cmd
  venv\Scripts\activate
  ```

When activated, your terminal will show `(venv)` at the beginning of the prompt.

### 3. Install Dependencies
Once the environment is active, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Deactivate the Virtual Environment
To stop using the virtual environment, deactivate it by running:

```bash
deactivate
```

---

### Additional Notes

- **Save New Dependencies**: After installing new packages, save them to `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```





# Setup Instructions for the Project

To run the initial setup and initialize the database for this project, follow the instruction below:

### Run the Database Initialization Script

Navigate to the project folder and execute the following command to run the database initialization script, which will set up the environment and create the necessary databases:

```bash
python3 scripts/initialize_db.py
```
