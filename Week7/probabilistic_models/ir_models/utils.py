from collections import Counter

def compute_probabilities(documents, queries):
    # Create a dictionary where each document ID maps to a Counter of its terms
    doc_terms = {doc_id: Counter(doc.split()) for doc_id, doc in documents.items()}
    # Calculate the total number of terms across all documents
    total_terms = sum(len(terms) for terms in doc_terms.values())

    probs = {}
    for query in queries:
        # Split the query into individual terms
        query_terms = query.split()
        for doc_id, terms in doc_terms.items():
            # Calculate the probability of the query given the document
            probs[(doc_id, query)] = sum(terms[term] / total_terms for term in query_terms if term in terms)
    return probs

def rank_documents(query, probabilities):
    # Sort documents based on their probability scores for the given query
    ranked_docs = sorted(
        [(doc_id, prob) for (doc_id, q), prob in probabilities.items() if q == query],
        key=lambda x: x[1],
        reverse=True
    )
    # Return a list of document IDs in descending order of their scores
    return [doc_id for doc_id, _ in ranked_docs]

def bayes_theorem(query, doc, joint_probs):
    # Calculate the numerator of Bayes' theorem
    numerator = joint_probs.get((query, doc, True), 0)
    # Calculate the denominator of Bayes' theorem
    denominator = sum(joint_probs.get((query, doc, rel), 0) for rel in [True, False])
    # Return the conditional probability
    return numerator / denominator if denominator else 0

def marginal_probability(joint_probs, condition):
    # Calculate the marginal probability based on a given condition
    return sum(prob for vars, prob in joint_probs.items() if condition(vars))