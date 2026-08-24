# Semantic Search Engine

## 🇬🇧 English

This is a semantic search engine for text documents using sentence embeddings and FAISS.

### Description

The system converts text documents into vector embeddings and finds documents or text fragments that are semantically similar to a user's query.

The project implements a complete semantic search pipeline:

* loads text documents from a dataset
* cleans and filters documents
* splits documents into overlapping text chunks
* generates sentence embeddings
* builds a FAISS vector index
* performs semantic similarity search
* returns the most relevant text fragments

### Search Pipeline

```text
Text Documents
      ↓
Document Loading
      ↓
Text Cleaning
      ↓
Text Chunking
      ↓
Sentence Embeddings
      ↓
FAISS Index
      ↓
Semantic Search
      ↓
Top-K Results
```

### Embedding Model

The project uses the `all-MiniLM-L6-v2` model from Sentence Transformers.

* Model: `all-MiniLM-L6-v2`
* Framework: Sentence Transformers
* Embedding-based semantic representation
* Embeddings are normalized before FAISS indexing

### Dataset

The project uses the **Plain Text Wikipedia (SimpleEnglish)** dataset available on Kaggle:

* https://www.kaggle.com/datasets/ffatty/plain-text-wikipedia-simpleenglish?resource=download

The dataset contains plain-text articles from Simple English Wikipedia.

### Data Processing

The preprocessing pipeline includes:

* loading documents from multiple dataset folders
* removing extremely short articles
* filtering documents containing excessive markup or garbage text
* splitting articles into chunks
* chunk size: 200 words
* overlap: 50 words
* minimum chunk size: 50 words

### Embeddings

Text chunks are converted into vector representations using Sentence Transformers.

The embeddings are generated with:

* Model: `all-MiniLM-L6-v2`
* Batch size: 64
* NumPy arrays for storing embeddings

The generated embeddings are saved as:

```text
embeddings/embeddings.npy
```

Text chunks are stored in:

```text
embeddings/chunks.pkl
```

### FAISS Index

FAISS is used for efficient vector similarity search.

The project uses:

* `IndexFlatIP`
* normalized embeddings
* inner product similarity

Since the vectors are L2-normalized, inner product corresponds to cosine similarity.

The resulting index is saved as:

```text
faiss/index.faiss
```

### Search

The search system accepts a natural-language query from the user.

For each query:

1. The query is converted into an embedding.
2. The embedding is normalized.
3. FAISS searches for the most similar vectors.
4. The top 10 results are returned.
5. Similarity scores and text fragments are displayed.

Example:

```text
Question: What is artificial intelligence?

Similarity: 0.7421
----------------------------------------------------------------------
Artificial intelligence is...
```

The program can be terminated using:

```text
exit
```

or:

```text
quit
```

### Features

* Semantic search instead of keyword-based search
* Sentence Transformer embeddings
* Overlapping document chunking
* FAISS vector similarity search
* Cosine similarity
* Top-K retrieval
* Automatic document preprocessing
* Local storage of embeddings and FAISS index
* Command-line search interface

### Technologies Used

* Python
* Sentence Transformers
* FAISS
* NumPy
* Pickle

### Project Structure

```text
semantic-search-engine/
│
├── dataset/
│   ├── 1of2/
│   └── 2of2/
│
├── embeddings/
│   ├── embeddings.npy
│   └── chunks.pkl
│
├── faiss/
│   └── index.faiss
│
├── utils.py
├── embeddings.py
├── faiss_index.py
├── search.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

### Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/semantic-search-engine.git
cd semantic-search-engine
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

First, generate embeddings:

```bash
python embeddings.py
```

Then create the FAISS index:

```bash
python faiss_index.py
```

Finally, start the semantic search:

```bash
python search.py
```

Enter a question or search query when prompted.

### Output

The system returns the most semantically relevant text fragments from the document collection along with their similarity scores.

---

## 🇷🇺 Русский

Это проект системы семантического поиска по текстовым документам с использованием эмбеддингов предложений и FAISS.

### Описание

Система преобразует текстовые документы в векторные представления и позволяет находить текстовые фрагменты, наиболее близкие к поисковому запросу по смыслу.

Проект реализует полный pipeline семантического поиска:

* загрузка текстовых документов
* очистка и фильтрация данных
* разделение документов на перекрывающиеся фрагменты
* создание эмбеддингов
* построение FAISS-индекса
* поиск по векторному сходству
* вывод наиболее релевантных фрагментов

### Pipeline поиска

```text
Текстовые документы
        ↓
Загрузка документов
        ↓
Очистка данных
        ↓
Разбиение на фрагменты
        ↓
Создание эмбеддингов
        ↓
FAISS-индекс
        ↓
Семантический поиск
        ↓
Top-K результатов
```

### Модель эмбеддингов

Для создания векторных представлений используется модель `all-MiniLM-L6-v2` из библиотеки Sentence Transformers.

* Модель: `all-MiniLM-L6-v2`
* Библиотека: Sentence Transformers
* Векторное представление текстов
* Нормализация эмбеддингов перед индексированием

### Данные

Используется датасет **Plain Text Wikipedia (SimpleEnglish)** с Kaggle:

* https://www.kaggle.com/datasets/ffatty/plain-text-wikipedia-simpleenglish?resource=download

Датасет содержит текстовые статьи из Simple English Wikipedia.

### Обработка данных

Pipeline предобработки включает:

* загрузку документов из нескольких папок
* удаление слишком коротких статей
* фильтрацию документов с большим количеством мусорной разметки
* разделение статей на фрагменты
* размер фрагмента: 200 слов
* перекрытие: 50 слов
* минимальный размер фрагмента: 50 слов

### Эмбеддинги

Каждый текстовый фрагмент преобразуется в вектор с помощью Sentence Transformers.

Параметры:

* модель: `all-MiniLM-L6-v2`
* размер batch: 64
* хранение эмбеддингов в формате NumPy

Эмбеддинги сохраняются в:

```text
embeddings/embeddings.npy
```

Текстовые фрагменты сохраняются в:

```text
embeddings/chunks.pkl
```

### FAISS-индекс

Для быстрого поиска по векторам используется библиотека FAISS.

Используется:

* `IndexFlatIP`
* нормализованные эмбеддинги
* сходство через inner product

Так как векторы нормализованы по L2-норме, inner product эквивалентен cosine similarity.

Индекс сохраняется в:

```text
faiss/index.faiss
```

### Поиск

Пользователь вводит естественно-языковой запрос.

Для каждого запроса:

1. Создаётся embedding запроса.
2. Вектор нормализуется.
3. FAISS выполняет поиск наиболее близких векторов.
4. Возвращаются 10 наиболее релевантных результатов.
5. Выводятся оценки сходства и найденные текстовые фрагменты.

Для завершения работы используются команды:

```text
exit
```

или:

```text
quit
```

### Возможности

* семантический поиск вместо поиска по ключевым словам
* создание эмбеддингов с помощью Sentence Transformers
* разбиение документов на перекрывающиеся фрагменты
* векторный поиск с использованием FAISS
* поиск по cosine similarity
* получение Top-K результатов
* автоматическая предобработка документов
* сохранение эмбеддингов и индекса
* консольный интерфейс поиска

### Технологии

* Python
* Sentence Transformers
* FAISS
* NumPy
* Pickle

### Структура проекта

```text
semantic-search-engine/
│
├── dataset/
│   ├── 1of2/
│   └── 2of2/
│
├── embeddings/
│   ├── embeddings.npy
│   └── chunks.pkl
│
├── faiss/
│   └── index.faiss
│
├── utils.py
├── embeddings.py
├── faiss_index.py
├── search.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

### Установка

Клонировать репозиторий:

```bash
git clone https://github.com/USERNAME/semantic-search-engine.git
cd semantic-search-engine
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

### Запуск

Сначала необходимо создать эмбеддинги:

```bash
python embeddings.py
```

Затем создать FAISS-индекс:

```bash
python faiss_index.py
```

После этого запустить семантический поиск:

```bash
python search.py
```

Введите поисковый запрос после появления приглашения `Question:`.

### Результат

Система возвращает наиболее релевантные текстовые фрагменты из коллекции документов вместе с оценкой их семантического сходства.
