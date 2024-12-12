from django.shortcuts import render
from retrieval.utils import create_term_document_matrix, search_documents_extended_boolean
from .models import Document

def search_documents(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        documents = Document.objects.all()
        term_document_matrix = create_term_document_matrix(documents)
        ranked_docs = search_documents_extended_boolean(query, documents, term_document_matrix)
        results = [{'document': doc, 'score': score} for doc, score in ranked_docs]
    return render(request, 'retrieval/search.html', {'query': query, 'results': results})