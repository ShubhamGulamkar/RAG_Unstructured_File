from ragas import evaluate
from ragas.metrics import faithfulness, context_precision

def evaluate_rag(dataset):
    result = evaluate(
        dataset,
        metrics=[faithfulness, context_precision]
    )
    return result