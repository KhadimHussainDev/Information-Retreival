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
    # words = [word for word in words if word not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return words

def create_term_document_matrix(documents):
    term_document_matrix = defaultdict(lambda: [0] * len(documents))
    for doc_index, doc in enumerate(documents):
        terms = preprocess_text(doc.content)
        for term in terms:
            term_document_matrix[term][doc_index] = 1
    return term_document_matrix

def search_documents_extended_boolean(query, documents, term_document_matrix):
    """
    Implements Extended Boolean search with AND, OR, NOT operations.
    Query format: "term1 and term2 not term3" or "term1 or term2 not term3"
    
    Args:
        query (str): The search query (e.g., "apple and mangos not juice")
        documents (list): List of documents to search through
        term_document_matrix (dict): Term-document matrix from create_term_document_matrix
    
    Returns:
        list: List of matching documents
    """
    # Convert query to lowercase and split into parts
    query_parts = query.lower().split()
    
    # Initialize variables to store terms
    positive_terms = []
    negative_terms = []
    operation = 'and'  # default operation
    
    # Parse query
    i = 0
    while i < len(query_parts):
        term = query_parts[i]
        
        if term in ('and', 'or'):
            operation = term
            i += 1
            continue
            
        if term == 'not':
            if i + 1 < len(query_parts):
                negative_terms.append(query_parts[i + 1])
                i += 2
            else:
                i += 1
            continue
            
        positive_terms.append(term)
        i += 1
    
    # Find matching documents
    matching_docs = []
    
    for doc_idx, doc in enumerate(documents):
        # Check positive terms based on operation
        matches_positive = False
        
        if operation == 'and':
            # All positive terms must be present
            matches_positive = all(
                term in term_document_matrix and 
                term_document_matrix[term][doc_idx] == 1 
                for term in positive_terms
            )
        else:  # OR operation
            # At least one positive term must be present
            matches_positive = any(
                term in term_document_matrix and 
                term_document_matrix[term][doc_idx] == 1 
                for term in positive_terms
            )
        
        # Check negative terms (NOT operation)
        # Document must not contain any negative terms
        matches_negative = all(
            term not in term_document_matrix or 
            term_document_matrix[term][doc_idx] == 0 
            for term in negative_terms
        )
        
        # Document must match positive terms criteria and not contain negative terms
        if matches_positive and matches_negative:
            matching_docs.append(doc)
    
    return [(doc, 1.0) for doc in matching_docs]  