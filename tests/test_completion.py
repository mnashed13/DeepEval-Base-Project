from deepeval import evaluate
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
from src.utils import get_completion

def test_completion_quality():
    prompt = "What is the capital of France?"
    completion = get_completion(prompt)
    
    # Test for hallucination
    hallucination_metric = HallucinationMetric(
        threshold=0.5,
        prompt=prompt,
        response=completion
    )
    
    # Test for answer relevancy
    relevancy_metric = AnswerRelevancyMetric(
        threshold=0.7,
        prompt=prompt,
        response=completion
    )
    
    # Run evaluation
    evaluation = evaluate([hallucination_metric, relevancy_metric])
    assert evaluation.success