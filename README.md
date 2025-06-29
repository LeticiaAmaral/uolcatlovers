markdown
# 🐱 UOLCatLovers - Extrator de Fatos sobre Gatos

Script Python que coleta fatos sobre gatos da API [Cat Facts](https://catfact.ninja/) e exporta para CSV.

## 📋 Pré-requisitos

- Python 3.8+
- Git (opcional)

## 🛠️ Configuração do Ambiente

1. *Clone o repositório*:
   ```bash
   git clone https://github.com/seu-usuario/uoicatlovers.git
   cd uoicatlovers

2. *Crie e ative um ambiente virtual (recomendado)*:
python -m venv venv

**Linux/Mac**:
source venv/bin/activate

**Windows**:
.\venv\Scripts\activate

4. *Instale as dependências*:
pip install -r requirements.txt


## 🚀 Como Usar
Execute o script principal:

python cat_facts.py

Isso irá:
    Coletar fatos de todas as páginas da API
    Gerar um arquivo cat_facts_<data>.csv
