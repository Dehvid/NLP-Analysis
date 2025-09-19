from flask import Flask, render_template, request
import spacy
from spacy.language import Language
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        text = request.form["text"]
        doc = nlp(text)
        
        # Sentence Boundary Detection (SBD)
        sentences = [sent.text for sent in doc.sents]
        
        # Tokenization, POS, Lemmatization, Attributes
        token_info = [{
            "text": token.text,
            "pos": token.pos_,
            "lemma": token.lemma_,
            "is_alpha": token.is_alpha,
            "shape": token.shape_,
            "is_stop": token.is_stop
        } for token in doc]
        
        # Named Entity Recognition
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Stemming and Stop word removal
        tokens = [token.text for token in doc if token.is_alpha]
        filtered = [w for w in tokens if w.lower() not in stop_words]
        stemmed = [stemmer.stem(w) for w in filtered]
        lemmatized = [lemmatizer.lemmatize(w) for w in filtered]

        # Vectorization (Bag of Words)
        vectorizer = CountVectorizer()
        vec = vectorizer.fit_transform([text])
        vectorized = dict(zip(vectorizer.get_feature_names_out(), vec.toarray()[0]))

        results = {
            "sentences": sentences,
            "token_info": token_info,
            "entities": entities,
            "filtered": filtered,
            "stemmed": stemmed,
            "lemmatized": lemmatized,
            "vectorized": vectorized
        }
        
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
