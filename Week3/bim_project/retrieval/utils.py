import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import defaultdict
from .models import Document

def preprocess_text(text):
    # Tokenization
    words = re.findall(r'\b\w+\b', text.lower())
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    print(words)
    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return words

def create_binary_vector(doc_terms, all_terms):
    return [1 if term in doc_terms else 0 for term in all_terms]

def get_documents_by_term(term):
    """
    Retrieves documents that contain the specified term.
    """
    documents = []
    for doc in Document.objects.all():
        content_terms = preprocess_text(doc.content)
        if term in content_terms:
            documents.append(doc)
    return documents

def get_non_overlapping_documents(terms):
    """
    Combines documents for multiple terms using set union.
    """
    combined_documents = set()
    for term in terms:
        documents_for_term = get_documents_by_term(term)
        combined_documents.update(documents_for_term)
    return list(combined_documents)



class DocumentGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, term, document):
        """Create an edge between a term and a document."""
        self.graph[term].append(document)

    def get_connected_documents(self, terms):
        """Retrieve all documents connected to the given terms."""
        connected_documents = set()
        for term in terms:
            if term in self.graph:
                connected_documents.update(self.graph[term])
        return list(connected_documents)

# Create a global graph instance
document_graph = DocumentGraph()

is_graph_built = False

def preprocess_and_build_graph():
    global is_graph_built
    if not is_graph_built:
        document_graph.graph.clear()  # Reset the graph
        for doc in Document.objects.all():
            content_terms = preprocess_text(doc.content)
            for term in content_terms:
                document_graph.add_edge(term, doc)
        is_graph_built = True

