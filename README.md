# 🎬 SentimentAI

</div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-enabled-blue?logo=docker)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8+-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-1.0+-blue.svg)

**🎬 [Demo ao Vivo](https://renanmrqs-sentimentai-app-j7ouwz.streamlit.app/) 🎬**

*Modelo de Machine Learning para análise de sentimentos em reviews de filmes usando Processamento de Linguagem Natural.*

</div>

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
- **FastAPI** - API REST para consumo de modelo

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
├── Dockerfile
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Instalação e Funcionamento via Docker 🐳


### Passo a Passo

**1. Construa a imagem:**
```bash
docker build -t sentimentai .
```

**2. Rode o container:**
```bash
docker run -p 8501:8501 sentimentai
```

**3. Acesse:**
http://localhost:8501

---

### 🐍 Instalação Manual

## Caso deseje rodar o projeto diretamente no seu ambiente python

**1. Clone o repositório e crie o venv:**
```
git clone https://github.com/Renanmrqs/SentimentAI.git
cd SentimentAI
python -m venv venv
```

**2. Instale as dependências e baixe os dados do NLTK:**
```
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

**3. Execute o App:**
```
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

## ⚙️ API

**APIRest desenvolvida com FastAPI, veja como rodar:**


**1. Inicie o servidor:**
```
uvicorn api:app --reload
```
**2. Acesse a documentação interativa (Swagger UI)**
```
http://localhost:8000/docs
```
**3. Exemplo de Requisição (CURL):**
```
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{"text": "This movie was absolutely amazing!"}'
```

---

## 🌐 Roadmap

- [✅] Suporte a tradução multi-idioma (PT-BR)
- [✅] Deploy no Streamlit Cloud
- [✅] Endpoint de API (FastAPI)
- [ ] Dashboard de visualização

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