1. **Entidades e Atributos**:
    - **Tipo_Sensor**
      - `id_tipo` (Chave Primária)
      - `nome`
      - `descricao`

    - **Sensor**
      - `id_sensor` (Chave Primária)
      - `id_tipo` (Chave Estrangeira para `Tipo_Sensor`)
      - `nome_sensor`
      - `localizacao`

    - **Medicao_Sensor**
      - `id_medicao` (Chave Primária)
      - `id_sensor` (Chave Estrangeira para `Sensor`)
      - `valor`
      - `data_hora`

    - **Rele**
      - `id_rele` (Chave Primária)
      - `nome_rele`
      - `localizacao`

    - **Status_Rele**
      - `id_status` (Chave Primária)
      - `id_rele` (Chave Estrangeira para `Rele`)
      - `estado`
      - `data_hora`

2. **Relacionamentos**:
    - **Tipo_Sensor** → **Sensor**: Um-para-Muitos (Um `Tipo_Sensor` pode estar associado a múltiplos registros de `Sensor`)
    - **Sensor** → **Medicao_Sensor**: Um-para-Muitos (Um `Sensor` pode ter múltiplos registros de `Medicao_Sensor`)
    - **Rele** → **Status_Rele**: Um-para-Muitos (Um `Rele` pode ter múltiplos registros de `Status_Rele`)
