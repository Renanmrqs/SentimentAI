# 🧠 SentimentAI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-enabled-blue?logo=docker)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8+-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-1.0+-blue.svg)

**🎬 [Demo ao Vivo](https://renanmrqs-sentimentai-app-j7ouwz.streamlit.app/) 🎬**

*Plataforma de Machine Learning para análise de linguagem natural — análise de sentimentos em reviews e detecção de comentários tóxicos.*

</div>

---

## 📊 Sobre o Projeto

O SentimentAI é uma API de NLP com dois modelos independentes:

| Modelo | Dataset | Tarefa | Acurácia |
|--------|---------|--------|----------|
| Sentimento | IMDB 50K Movie Reviews | Classifica reviews como positivas ou negativas | 89.2% |
| Toxicidade | Jigsaw Toxic Comment Dataset | Detecta comentários tóxicos ou seguros | 89.0% |

Ambos os modelos usam **Regressão Logística + TF-IDF** e estão disponíveis via API REST.

---

## 🚀 Funcionalidades

- ✅ Pré-processamento de texto (remoção de HTML, stopwords)
- ✅ Vetorização TF-IDF (5000 features)
- ✅ Análise de sentimento em tempo real
- ✅ Detecção de toxicidade em comentários
- ✅ Interface web com Streamlit
- ✅ Suporte multi-idioma (EN/PT via tradução automática)

---

## 🛠️ Tecnologias

- **Python 3.8+**
- **scikit-learn** - Machine Learning
- **NLTK** - Processamento de Linguagem Natural
- **Pandas** - Manipulação de dados
- **Streamlit** - Interface web
- **FastAPI** - API REST

---

## 📁 Estrutura do Projeto

```
SentimentAI/
├── assets/              # Imagens e recursos
├── data/
│   ├── IMDB Dataset.csv
│   ├── IMDB_Cleaned.csv
│   ├── 2018_train_data.csv
│   └── toxic_comments_cleaned.csv
├── models/
│   ├── sentiment_model.pkl
│   ├── vectorizer.pkl
│   ├── toxic_model.pkl
│   └── toxic_vectorizer.pkl
├── notebooks/
├── src/
│   ├── exploration.py
│   ├── preprocessing.py
│   ├── training.py
│   └── utils.py
├── venv/
├── app.py
├── api.py
├── Dockerfile
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ API

**🔌 [Documentação da API (Swagger)](https://sentimentai-api.onrender.com/docs)**

### Rotas disponíveis

**POST `/predict`** — Análise de sentimento (reviews)
```bash
curl -X 'POST' \
  'https://sentimentai-api.onrender.com/predict' \
  -H 'Content-Type: application/json' \
  -d '{"text": "This movie was absolutely amazing!"}'
```
```json
{
  "sentiment": "positive",
  "trust": 0.94
}
```

---

**POST `/toxic_predict`** — Detecção de toxicidade (comentários)
```bash
curl -X 'POST' \
  'https://sentimentai-api.onrender.com/toxic_predict' \
  -H 'Content-Type: application/json' \
  -d '{"text": "I hate you so much"}'
```
```json
{
  "toxic": "toxic",
  "trust": 0.99
}
```

> A API está hospedada no plano gratuito do Render e pode demorar alguns segundos para responder na primeira requisição.

---

## ⚙️ Como Rodar Localmente

### Via Docker 🐳

```bash
docker build -t sentimentai .
docker run -p 8501:8501 sentimentai
```
Acesse: `http://localhost:8501`

### Manual 🐍

```bash
git clone https://github.com/Renanmrqs/SentimentAI.git
cd SentimentAI
python -m venv venv
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
streamlit run app.py
```

Para rodar a API:
```bash
uvicorn api:app --reload
```

---

## 📈 Performance dos Modelos

**Modelo de Sentimento (IMDB)**
```
Acurácia: 89.2%

              precision    recall  f1-score   support
    negative       0.88      0.89      0.88      5000
    positive       0.89      0.88      0.88      5000
```

**Modelo de Toxicidade (Jigsaw)**
```
Acurácia: 89.0%

              precision    recall  f1-score   support
        safe       0.88      0.91      0.89      3240
       toxic       0.90      0.87      0.89      3249
```

---

## 💡 Como Funciona

**1. Pré-processamento**
```
Entrada: "This movie was AMAZING!!! <br> I loved it."
Saída:   "movie amazing loved"
```
- Conversão para minúsculas
- Remoção de tags HTML
- Remoção de pontuação e caracteres especiais
- Filtragem de stopwords

**2. Vetorização TF-IDF**
```
"movie amazing" → [0.0, 0.52, 0.0, 0.71, ...]
```

**3. Classificação**
```
[0.0, 0.52, ...] → Regressão Logística → resultado + confiança
```

---

## 🌐 Roadmap

- [✅] Modelo de análise de sentimentos
- [✅] Deploy no Streamlit Cloud
- [✅] API REST com FastAPI
- [✅] Suporte multi-idioma (PT-BR)
- [✅] Modelo de detecção de toxicidade
- [✅] Rota `/toxic_predict`
- [ ] Dashboard de visualização
- [ ] Retreinar com datasets maiores

---

## 🔗 Projetos que usam esta API

- **[ToxiBlock](https://github.com/Renanmrqs/ToxiBlock)** — Extensão de navegador que usa o `/toxic_predict` para ocultar comentários tóxicos em páginas da web

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

- [IMDB 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- [Jigsaw Toxic Comment Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)