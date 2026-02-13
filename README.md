# 🎬 SentimentAI

Modelo de Machine Learning para análise de sentimentos em reviews de filmes usando Processamento de Linguagem Natural.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)

---

## 📊 Sobre o Projeto

Classifica reviews de filmes como **positivas** ou **negativas** com ~89% de acurácia usando Machine Learning.

**Dataset:** IMDB 50K Movie Reviews  
**Modelo:** Regressão Logística + TF-IDF  
**Acurácia:** 89.2%

---

## 🚀 Funcionalidades

- ✅ Pré-processamento de texto (remoção de HTML, stopwords)
- ✅ Vetorização TF-IDF (5000 features)
- ✅ Previsão de sentimento em tempo real
- ✅ Interface web com Streamlit
- ✅ Suporte multi-idioma (EN/PT)

---

## 🛠️ Tecnologias

- **Python 3.8+**
- **scikit-learn** - Machine Learning
- **NLTK** - Processamento de Linguagem Natural
- **Pandas** - Manipulação de dados
- **Streamlit** - Interface web

---

## 📁 Estrutura do Projeto
```
SentimentAI/
├── assets/              # Imagens e recursos
├── data/
│   ├── IMDB Dataset.csv
│   └── IMDB_Cleaned.csv
├── models/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
├── notebooks/           # Jupyter notebooks (opcional)
├── src/
│   ├── exploration.py
│   ├── preprocessing.py
│   ├── training.py
│   └── utils.py
├── venv/                # Ambiente virtual (não versionado)
├── app.py               # Interface Streamlit
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip

### Passo a Passo

**1. Clone o repositório:**
```bash
git clone https://github.com/Renanmrqs/SentimentAI.git
cd SentimentAI
```

**2. Crie um ambiente virtual:**
```bash
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Baixe os dados do NLTK:**
```bash
python -c "import nltk; nltk.download('stopwords')"
```

---

## 🎯 Como Usar

### Opção 1: Usar o modelo já treinado (recomendado)
```bash
streamlit run app.py
```

Acesse: `http://localhost:8501`

### Opção 2: Treinar do zero
```bash
# 1. Explorar dados
python src/exploration.py

# 2. Pré-processar dataset
python src/preprocessing.py

# 3. Treinar modelo
python src/training.py

# 4. Rodar aplicação
streamlit run app.py
```

---

## 📈 Performance do Modelo
```
Acurácia: 89.2%

              precision    recall  f1-score   support
    negative       0.88      0.89      0.88      5000
    positive       0.89      0.88      0.88      5000

    accuracy                           0.89     10000
```

---

## 💡 Como Funciona

**1. Pré-processamento de Texto**
```
Entrada: "This movie was AMAZING!!! <br> I loved it."
Saída: "movie amazing loved"
```
- Conversão para minúsculas
- Remoção de tags HTML
- Remoção de pontuação
- Filtragem de stopwords

**2. Vetorização (TF-IDF)**
```
Texto → Vetor numérico (5000 features)
"movie amazing" → [0.0, 0.52, 0.0, 0.71, ...]
```

**3. Classificação**
```
Vetor → Regressão Logística → Sentimento + Confiança
[0.0, 0.52, ...] → "positive" (94.2%)
```

---

## 🌐 Roadmap

- [ ] Suporte a tradução multi-idioma (PT-BR)
- [ ] Deploy no Streamlit Cloud
- [ ] Dashboard de visualização
- [ ] Endpoint de API (FastAPI)

---

## 📧 Contato

**Renan Fernandes Marques**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/renan-fernandes-marques)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/Renanmrqs)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:renanmarques1923@gmail.com)

---

## 📜 Licença

Este projeto é open source para fins educacionais.

---

⭐ **Se este projeto te ajudou, considere dar uma estrela!**

---

## 🙏 Agradecimentos

- Dataset: [IMDB 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- Inspiração: CS50's Introduction to AI with Python