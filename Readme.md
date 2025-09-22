
#  NLP Analysis Tool

A simple **Flask web app** that demonstrates various Natural Language Processing (NLP) techniques such as sentence boundary detection, tokenization, POS tagging, lemmatization, stemming, named entity recognition (NER), and bag-of-words vectorization.

---

## Features

* Sentence Boundary Detection (SBD)
* Tokenization & Part-of-Speech tagging
* Lemmatization & Stemming
* Stopword removal
* Named Entity Recognition (NER)
* Bag-of-Words vectorization
* Clean web interface built with Flask + HTML/CSS

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/YourUsername/projectnlp.git
cd projectnlp
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\\Scripts\\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK data

Open a Python shell and run:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
```

### 5. Download SpaCy model

```bash
python -m spacy download en_core_web_sm
```

---

## Usage

Run the Flask server:

```bash
python index.py
```

Then open in your browser:

```
http://127.0.0.1:5000
```

---

## Project Structure

```
projectnlp/
│── index.py              # Main Flask app
│── templates/
│   └── index.html        # Frontend HTML template     
│── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## Screenshot

*(Add a screenshot of your app here if possible!)*

---

## Requirements

* Python 3.8+
* Flask
* SpaCy
* NLTK
* Scikit-learn

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## License

This project is open source under the **MIT License**.

---
