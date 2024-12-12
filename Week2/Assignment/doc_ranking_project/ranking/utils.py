import os
from sklearn.feature_extraction.text import TfidfVectorizer
import math
from collections import Counter
from spellchecker import SpellChecker
import string
import re

def load_documents():
    documents = []
    documents_dir = os.path.join(os.path.dirname(__file__), 'documents')
    for filename in os.listdir(documents_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(documents_dir, filename), 'r') as file:
                documents.append({'title': filename, 'content': file.read()})
    return documents

def search_documents(query, documents):
    query_keywords = query.lower().split()
    ranked_documents = []

    for doc in documents:
        content = doc['content'].lower()
        match_count = sum(keyword in content for keyword in query_keywords)
        if match_count > 0:
            ranked_documents.append({'title': doc['title'], 'content': doc['content'], 'score': match_count})

    # Sort documents by score in descending order
    ranked_documents.sort(key=lambda x: x['score'], reverse=True)
    return ranked_documents


def compute_tf(document):
    tf = Counter(document)
    total_terms = len(document)
    for term in tf:
        tf[term] = tf[term] / total_terms
    return tf

def compute_idf(documents):
    idf = {}
    total_documents = len(documents)
    all_terms = set(term for doc in documents for term in doc)
    for term in all_terms:
        containing_docs = sum(1 for doc in documents if term in doc)
        idf[term] = math.log(total_documents / (1 + containing_docs))
    return idf

def compute_tfidf(tf, idf):
    tfidf = {}
    for term, tf_value in tf.items():
        tfidf[term] = tf_value * idf.get(term, 0)
    return tfidf

def cosine_similarity(doc_tfidf, query_tfidf):
    dot_product = sum(doc_tfidf.get(term, 0) * query_tfidf.get(term, 0) for term in query_tfidf)
    doc_norm = math.sqrt(sum(value ** 2 for value in doc_tfidf.values()))
    query_norm = math.sqrt(sum(value ** 2 for value in query_tfidf.values()))
    if doc_norm == 0 or query_norm == 0:
        return 0.0
    return dot_product / (doc_norm * query_norm)



def search_documents_tfidf(query, documents, preprocess=False, ignore_spelling=False):
    if preprocess:
        query_terms = preprocess_text(query, ignore_spelling)
    else:
        query_terms = query.lower().split()

    corpus = [doc['content'].lower().split() for doc in documents]
    titles = [doc['title'] for doc in documents]

    tf_corpus = [compute_tf(doc) for doc in corpus]
    idf = compute_idf(corpus)
    tfidf_corpus = [compute_tfidf(tf, idf) for tf in tf_corpus]

    query_tf = compute_tf(query_terms)
    query_tfidf = compute_tfidf(query_tf, idf)

    scores = [cosine_similarity(doc_tfidf, query_tfidf) for doc_tfidf in tfidf_corpus]

    ranked_documents = []
    for idx, score in enumerate(scores):
        if score > 0:
            highlighted_content = highlight_terms(' '.join(corpus[idx]), query_terms)
            ranked_documents.append({'title': titles[idx], 'content': highlighted_content, 'score': score})

    ranked_documents.sort(key=lambda x: x['score'], reverse=True)
    return ranked_documents

def highlight_terms(content, terms):
    for term in terms:
        # Use word boundaries (\b) to match whole words
        content = re.sub(rf'\b{re.escape(term)}\b', f'<span class="highlight">{term}</span>', content, flags=re.IGNORECASE)
    return content

spell = SpellChecker()
def preprocess_text(text, ignore_spelling=False):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    words = text.split()

    # Correct spelling if ignoring spelling mistakes
    if ignore_spelling:
        words = [spell.correction(word) for word in words]
    return words