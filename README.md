# DeepEval Base Project

This project serves as a foundation for evaluating Large Language Models (LLMs) using [DeepEval](https://docs.deepeval.com/), a comprehensive framework for testing and evaluating LLM applications.

## 🚀 Getting Started

1. Clone this repository
2. Install dependencies:

```bash
pip install deepeval
```

3. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## 📁 Project Structure

```
DeepEval-Base-Project/
├── tests/                    # Your evaluation test cases
│   ├── test_relevancy.py    # Answer and contextual relevancy tests
│   ├── test_consistency.py  # Factual consistency tests
│   └── test_bias.py        # Bias evaluation tests
├── data/                    # Test datasets and examples
│   ├── questions.json      # Test questions
│   └── contexts.json       # Test contexts
├── configs/                 # Configuration files
│   └── eval_config.yaml    # Evaluation parameters and thresholds
└── results/                # Evaluation results and reports
```

## 💡 How to Use This Repository

1. **Configure Your Evaluation Settings**

   - Navigate to `configs/eval_config.yaml`
   - Set your desired thresholds for each metric
   - Configure API keys and model settings

2. **Add Your Test Cases**

   ```python
   # tests/test_relevancy.py
   from deepeval.test_case import LLMTestCase
   from deepeval.metrics import AnswerRelevancy

   def test_answer_relevancy():
       test_case = LLMTestCase(
           input="What is the capital of France?",
           actual_output="Paris is the capital of France",
           expected_output="Paris"
       )

       metric = AnswerRelevancy()
       assert metric.measure(test_case) >= 0.7
   ```

3. **Prepare Your Data**

   - Add your test questions to `data/questions.json`
   - If using RAG, add your contexts to `data/contexts.json`
   - Structure your data files according to your needs

4. **Run Evaluations**

   ```bash
   # Run all tests
   python -m pytest tests/

   # Run specific test category
   python -m pytest tests/test_relevancy.py
   ```

5. **View Results**
   - Check the `results/` directory for detailed evaluation reports
   - Results include scores for each metric and overall performance

## 🔍 Common Use Cases

1. **RAG Evaluation**

   ```python
   from deepeval.metrics import ContextualRelevancy

   metric = ContextualRelevancy()
   result = metric.measure(
       context="Paris is the capital of France and known for the Eiffel Tower.",
       question="What is Paris known for?",
       response="Paris is known for the Eiffel Tower."
   )
   ```

2. **Batch Testing**

   ```python
   from deepeval import evaluate_all
   from deepeval.test_case import LLMTestCase

   test_cases = [
       LLMTestCase(...),
       LLMTestCase(...),
   ]
   results = evaluate_all(test_cases, metrics=[AnswerRelevancy()])
   ```

## 📊 Common Evaluation Metrics

DeepEval provides several powerful metrics for evaluating LLM outputs:

### Answer Relevancy

- [Answer Relevancy Documentation](https://docs.deepeval.com/metrics/answer-relevancy)
- Measures how well an LLM's response aligns with the given question
- Useful for question-answering and chatbot applications

### Contextual Relevancy

- [Contextual Relevancy Documentation](https://docs.deepeval.com/metrics/contextual-relevancy)
- Evaluates if the LLM's response uses the provided context appropriately
- Essential for RAG (Retrieval-Augmented Generation) applications

### Factual Consistency

- [Factual Consistency Documentation](https://docs.deepeval.com/metrics/factual-consistency)
- Checks if the LLM's response contains factual contradictions with the given context
- Critical for ensuring truthful and accurate responses

### Response Completeness

- [Response Completeness Documentation](https://docs.deepeval.com/metrics/response-completeness)
- Assesses whether the LLM's response fully addresses all aspects of the question
- Important for comprehensive answer generation

### Bias Evaluation

- [Bias Evaluation Documentation](https://docs.deepeval.com/metrics/bias)
- Detects potential biases in LLM outputs
- Essential for ensuring fair and ethical AI responses

## 🛠️ Example Usage

```python
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancy, ContextualRelevancy

# Example evaluation
metric = AnswerRelevancy()
result = metric.measure(
    question="What is machine learning?",
    response="Machine learning is a subset of artificial intelligence...",
)
```

## 📚 Additional Resources

- [DeepEval Documentation](https://docs.deepeval.com/)
- [DeepEval GitHub Repository](https://github.com/confident-ai/deepeval)
- [DeepEval Examples](https://docs.deepeval.com/examples)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
