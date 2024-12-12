from django.shortcuts import render
from .models import Document
from .utils import preprocess_text, create_binary_vector
import numpy as np
from .utils import get_non_overlapping_documents
from .utils import document_graph
from .utils import preprocess_and_build_graph

def search_documents(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        query_terms = preprocess_text(query)
        all_terms = list(set(term for doc in Document.objects.all() for term in preprocess_text(doc.content)))
        query_vector = create_binary_vector(query_terms, all_terms)

        # Score Documents
        for doc in Document.objects.all():
            doc_vector = create_binary_vector(preprocess_text(doc.content), all_terms)
            score = np.dot(query_vector, doc_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(doc_vector))
            if(score>0):
                results.append({'document': doc, 'score': score})

        # Sort by score
        results = sorted(results, key=lambda x: x['score'], reverse=True)[:5]  # Top-5 results

    return render(request, 'retrieval/search.html', {'query': query, 'results': results})


def search_non_overlapping_documents(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        terms = preprocess_text(query)  # Preprocess the query to extract terms
        results = get_non_overlapping_documents(terms)

    return render(request, 'retrieval/search_non_overlap.html', {'query': query, 'results': results})


def search_proximal_nodes(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        preprocess_and_build_graph()  # Build or update the graph when needed
        terms = preprocess_text(query)  # Preprocess query terms
        results = document_graph.get_connected_documents(terms)

    return render(request, 'retrieval/search_proximal_nodes.html', {'query': query, 'results': results})
