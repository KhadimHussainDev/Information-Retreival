from django.shortcuts import render
from django.shortcuts import render
from .utils import compute_probabilities, rank_documents, bayes_theorem

# Create your views here.
documents = {
    1: "Python is a popular programming language.",
    2: "Machine learning is a subset of AI.",
    3: "Deep learning uses neural networks."
}

queries = ["What is Python?", "Explain machine learning."]

relevance = {
    (1, "What is Python?"): 1,
    (2, "Explain machine learning."): 1,
    (3, "Explain machine learning."): 0
}

def interference_model_view(request):
    probabilities = compute_probabilities(documents, queries)
    ranked_docs = rank_documents("What is Python?", probabilities)
    return render(request, 'index.html', {'ranked_docs': ranked_docs})

def belief_network_view(request):
    joint_probs = {
        ("What is Python?", 1, True): 0.6,
        ("What is Python?", 1, False): 0.4,
    }
    prob = bayes_theorem("What is Python?", 1, joint_probs)
    return render(request, 'index.html', {'prob': prob})
