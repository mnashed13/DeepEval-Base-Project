from deepeval import evaluate
from deepeval.metrics import ContextualRelevancyMetric
from src.utils import get_rag_completion

def test_rag_retrieval():
    query = "What are the company's policies on remote work?"
    context = "Our company allows flexible remote work arrangements..."
    completion = get_rag_completion(query, context)
    
    contextual_relevancy = ContextualRelevancyMetric(
        threshold=0.7,
        context=context,
        prompt=query,
        response=completion
    )
    
    evaluation = evaluate([contextual_relevancy])
    assert evaluation.success