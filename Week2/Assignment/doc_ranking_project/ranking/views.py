from django.shortcuts import render
from .utils import load_documents, search_documents_tfidf

def home(request):
    documents = load_documents()
    query = request.GET.get('query', '')
    preprocess = request.GET.get('preprocess', 'false').lower() == 'on'
    ignore_spelling = request.GET.get('ignore_spelling', 'false').lower() == 'on'
    results = []

    if query:
        results = search_documents_tfidf(query, documents, preprocess=preprocess, ignore_spelling=ignore_spelling)

    return render(request, 'ranking/home.html', {'query': query, 'results': results, 'preprocess': preprocess, 'ignore_spelling': ignore_spelling})